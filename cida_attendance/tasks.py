import datetime
from logging import getLogger

from cida_attendance.client import HttpClient, HttpClientError
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

    last_event_time = None

    if last_event_time:
        start_date = last_event_time[0].astimezone(
            local_time.tzinfo
        ) + datetime.timedelta(seconds=1)
    else:
        start_date = datetime.datetime(2000, 1, 1, tzinfo=local_time.tzinfo)


    def on_data(data):
        by_employee_no = (
            bytes(data.struAcsEventInfo.byEmployeeNo)
            .decode("ascii")
            .rstrip("\x00")
        )
        if by_employee_no:
            print(
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

    logger.info("Events synchronized")
    return session.logout()


AUTH_TOKEN = "qEMtk8a/2RvwZbdnJu0Y0gL1PqCPOy3bnNxmpf9rT18="
URL = "http://cidata.gob.ve/b/sync_attendance.php"


AUTH_TOKEN = "your_auth_token_here"
URL = "http://localhost:8080/sync_attendance.php"


def synchronize_http():
    logger.info("Starting HTTP synchronization...")

    client = HttpClient(auth_token=AUTH_TOKEN, url=URL)

    try:
        if data := client.get():
            last_sync = data.get("last_sync")
            print("Last sync:", last_sync, data)
        else:
            return False
    except HttpClientError as e:
        logger.error("HTTP error: %s", e)
        return False

    device_data = {
        "device_id": "your_device_id",
        "device_model": "your_device_model",
        "device_name": "your_device_name",
        "records": [
            {
                "employee_id": f"emp_{index}",
                "timestamp": (
                    datetime.datetime.now(datetime.timezone.utc)
                    - datetime.timedelta(minutes=index)
                ).isoformat(),
                "event_type": 1,
                "event_minor": 0,
            }
            for index in range(200)
        ],
    }

    try:
        response = client.post(device_data)
        logger.info("Server response: %s", response)
    except HttpClientError as e:
        logger.error("HTTP error: %s", e)
        return False

    logger.info("HTTP synchronization completed.")
    return True


if __name__ == "__main__":
    synchronize()
