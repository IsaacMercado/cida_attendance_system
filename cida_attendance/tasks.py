import ctypes
import datetime
from logging import getLogger
from xml.etree import ElementTree as ET
import re

import psycopg

from cida_attendance.config import load_config
from cida_attendance.constants import NET_DVR_GET_ACS_EVENT
from cida_attendance.structures import (
    NET_DVR_ACS_EVENT_CFG,
    NET_DVR_ACS_EVENT_COND,
    NET_DVR_DEVICEINFO_V40,
    NET_DVR_USER_LOGIN_INFO,
)
from cida_attendance.utils import (
    NET_DVR_RemoteConfig,
    dll,
    get_last_error,
    net_dvr_xml_config,
)

logger = getLogger(__name__)


def check_db() -> bool:
    logger.info("Checking database...")
    config = load_config()
    if not config["uri_db"]:
        return False
    try:
        with psycopg.connect(config["uri_db"]):
            pass
        logger.info("Database checked")
        return True
    except psycopg.Error as error:
        logger.error(
            "Error: %s",
            error,
            exc_info=error,
        )
        return False


def check_device():
    logger.info("Checking device...")
    dll.NET_DVR_Init()
    dll.NET_DVR_SetConnectTime(2000, 1)
    dll.NET_DVR_SetReconnect(10000, True)

    config = load_config()

    login_info = NET_DVR_USER_LOGIN_INFO.login(
        config["ip"].encode("ascii"),
        config["user"].encode("ascii"),
        config["password"].encode("ascii"),
        config["port"],
    )
    device_info = NET_DVR_DEVICEINFO_V40()
    user_id = dll.NET_DVR_Login_V40(
        ctypes.byref(login_info),
        ctypes.byref(device_info),
    )

    logger.info("User ID: %s", user_id)

    if user_id < 0:
        dll.NET_DVR_Cleanup()
        logger.error(
            "Error code: %d, %s",
            *get_last_error(),
        )
        return False

    dll.NET_DVR_Logout(user_id)
    dll.NET_DVR_Cleanup()
    logger.info("Device checked")
    return True


def synchronize():
    logger.info("Synchronizing...")
    config = load_config()

    dll.NET_DVR_Init()
    dll.NET_DVR_SetConnectTime(2000, 1)
    dll.NET_DVR_SetReconnect(10000, True)

    login_info = NET_DVR_USER_LOGIN_INFO.login(
        config["ip"].encode("ascii"),
        config["user"].encode("ascii"),
        config["password"].encode("ascii"),
        config["port"],
    )
    device_info = NET_DVR_DEVICEINFO_V40()
    user_id = dll.NET_DVR_Login_V40(
        ctypes.byref(login_info),
        ctypes.byref(device_info),
    )

    logger.info("User ID: %s", user_id)

    if user_id < 0:
        logger.error(
            "Error code: %d, %s",
            *get_last_error(),
        )
        dll.NET_DVR_Cleanup()
        return

    with psycopg.connect(config["uri_db"]) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT to_regclass('cida_attendance')")

            if not cursor.fetchone()[0]:
                logger.warning("Table cida_attendance does not exist")
                logger.info("Creating table cida_attendance")
                cursor.execute(
                    """
                    CREATE TABLE cida_attendance (
                        id SERIAL PRIMARY KEY,
                        event_user_id VARCHAR(100) NOT NULL,
                        event_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                        event_type INTEGER NOT NULL,
                        device_model VARCHAR(100) NOT NULL,
                        device_serial VARCHAR(100) NOT NULL,
                        device_name VARCHAR(100)
                    );
                    """
                )

            time_xml = ET.fromstring(
                net_dvr_xml_config(
                    user_id,
                    "GET /ISAPI/System/time",
                ).decode("ascii")
            )
            namespace = {"ns": time_xml.tag.split("}")[0].strip("{")}
            stz = time_xml.find("ns:timeZone", namespace).text

            mtz = re.match(r"([A-Z]+)([-+]\d+):(\d+):(\d+)", stz)

            if mtz:
                gtz = mtz.groups()
                tz = datetime.timezone(
                    datetime.timedelta(
                        hours=int(gtz[1]),
                        minutes=int(gtz[2]),
                        seconds=int(gtz[3]),
                    ),
                    name=gtz[0],
                )
            else:
                tz = datetime.timezone.utc

            device_xml = ET.fromstring(
                net_dvr_xml_config(
                    user_id,
                    "GET /ISAPI/System/deviceInfo",
                ).decode("ascii")
            )

            namespace = {"ns": device_xml.tag.split("}")[0].strip("{")}
            model = device_xml.find("ns:model", namespace).text
            serial = device_xml.find("ns:serialNumber", namespace).text

            cursor.execute(
                """
                SELECT event_time
                FROM cida_attendance
                WHERE device_serial = %s AND device_model = %s
                ORDER BY event_time DESC
                LIMIT 1
                """,
                (serial, model),
            )
            last_event_time = cursor.fetchone()

            if last_event_time:
                start_date = last_event_time[0].astimezone(tz) + datetime.timedelta(
                    seconds=1
                )
            else:
                start_date = datetime.datetime(2000, 1, 1, tzinfo=tz)

            cond = NET_DVR_ACS_EVENT_COND()

            cond.dwMajor = 0x5
            cond.dwMinor = 0x26

            end_date = datetime.datetime.now(tz)

            cond.struStartTime.from_datetime(start_date)
            cond.struEndTime.from_datetime(end_date)

            events = []

            NET_DVR_RemoteConfig(
                user_id,
                NET_DVR_GET_ACS_EVENT,
                cond,
                on_data=lambda data: events.append(
                    (
                        (
                            bytes(data.struAcsEventInfo.byEmployeeNo)
                            .decode("ascii")
                            .rstrip("\x00")
                        ),
                        data.struTime.to_python(tz),
                        data.struAcsEventInfo.byAttendanceStatus,
                        model,
                        serial,
                        config["name"],
                    )
                ),
                data_cls=NET_DVR_ACS_EVENT_CFG,
            )
            cursor.executemany(
                """
                INSERT INTO cida_attendance (event_user_id, event_time, event_type, device_model, device_serial, device_name)
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                events,
            )

            conn.commit()
            logger.info("Events synchronized")

    dll.NET_DVR_Logout(user_id)
    dll.NET_DVR_Cleanup()
    return True
