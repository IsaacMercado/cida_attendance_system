import ctypes
import datetime
from logging import getLogger
from xml.etree import ElementTree as ET

import psycopg

from cida_attendance.config import load_config
from cida_attendance.structures import (
    NET_DVR_DEVICEINFO_V40,
    NET_DVR_USER_LOGIN_INFO,
)
from cida_attendance.utils import dll, get_last_error, net_dvr_xml_config, search_events

logger = getLogger(__name__)


def check_db() -> bool:
    logger.info("Checking database...")
    config = load_config()
    if not config["uri_db"]:
        return False
    try:
        with psycopg.connect(config["uri_db"]):
            pass
        return True
    except psycopg.Error:
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

    if user_id < 0:
        dll.NET_DVR_Cleanup()
        return False

    dll.NET_DVR_Logout(user_id)
    dll.NET_DVR_Cleanup()
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
                print("Table does not exist")
                return

    with psycopg.connect(config["uri_db"]) as conn:
        with conn.cursor() as cursor:
            if not cursor.fetchone()[0]:
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

            xml = ET.fromstring(
                net_dvr_xml_config(
                    user_id,
                    "GET /ISAPI/System/deviceInfo",
                ).decode("ascii")
            )

            device_data = xml.find("deviceInfo")
            model = device_data.find("model").text
            serial = device_data.find("serialNumber").text

            # get last event_time
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
                last_event_time = last_event_time[0]
            else:
                last_event_time = datetime.datetime.min

            events = search_events(
                user_id,
                last_event_time,
                datetime.datetime.now().replace(hour=23, minute=59, second=59),
            )

            cursor.executemany(
                """
                INSERT INTO cida_attendance (event_user_id, event_time, event_type, device_model, device_serial, device_name)
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                [
                    (
                        bytes(event.struAcsEventInfo.byEmployeeNo).decode("ascii"),
                        event.struTime.to_python(),
                        event.struAcsEventInfo.byAttendanceStatus,
                        model,
                        serial,
                        config["name"],
                    )
                    for event in events
                ],
            )

            conn.commit()

    dll.NET_DVR_Logout(user_id)
    dll.NET_DVR_Cleanup()
