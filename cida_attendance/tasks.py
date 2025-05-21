import datetime
from logging import getLogger

import psycopg

from cida_attendance.config import load_config
from cida_attendance.constants import NET_DVR_GET_ACS_EVENT
from cida_attendance.session import Session
from cida_attendance.structures import NET_DVR_ACS_EVENT_CFG, NET_DVR_ACS_EVENT_COND
from cida_attendance.utils import cleanup_dll, init_dll

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

    config = load_config()
    init_dll()
    session = Session()

    if not session.login(**config):
        cleanup_dll()
        return False

    logger.info("Device checked")
    return session.logout()


def synchronize():
    logger.info("Synchronizing...")
    config = load_config()
    init_dll()
    session = Session()

    if not session.login(**config):
        cleanup_dll()
        return False

    model, serial = session.get_device_info()
    local_time, tz = session.get_device_time()
    logger.info("Device model: %s", model)

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
                        device_name VARCHAR(100),
                        event_minor INTEGER NOT NULL DEFAULT 0
                    );
                    """
                )
                conn.commit()

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
                start_date = last_event_time[0].astimezone(
                    local_time.tzinfo
                ) + datetime.timedelta(seconds=1)
            else:
                start_date = datetime.datetime(2000, 1, 1, tzinfo=local_time.tzinfo)

            with cursor.copy(
                "COPY cida_attendance "
                "(event_user_id, event_time, event_type, device_model, device_serial, device_name, event_minor) "
                "FROM STDIN"
            ) as copy:

                def on_data(data):
                    by_employee_no = (
                        bytes(data.struAcsEventInfo.byEmployeeNo)
                        .decode("ascii")
                        .rstrip("\x00")
                    )
                    if by_employee_no:
                        copy.write_row(
                            (
                                by_employee_no,
                                data.struTime.to_python(local_time.tzinfo),
                                data.struAcsEventInfo.byAttendanceStatus,
                                model,
                                serial,
                                config["name"],
                                data.dwMinor,
                            )
                        )

                session.run_remote_config(
                    NET_DVR_GET_ACS_EVENT,
                    NET_DVR_ACS_EVENT_COND().from_python(
                        major=0x5,
                        # minor=0x26,
                        # minor=0x01,
                        start_time=start_date,
                        end_time=local_time,
                    ),
                    on_data=on_data,
                    data_cls=NET_DVR_ACS_EVENT_CFG,
                )

            conn.commit()
            logger.info("Events synchronized")

    return session.logout()
