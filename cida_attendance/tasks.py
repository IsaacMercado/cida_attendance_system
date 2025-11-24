import datetime
from logging import getLogger

from cida_attendance.client import HttpClient, HttpClientError
from cida_attendance.config import load_config
from cida_attendance.constants import NET_DVR_GET_ACS_EVENT
from cida_attendance.session import Session
from cida_attendance.structures import NET_DVR_ACS_EVENT_CFG, NET_DVR_ACS_EVENT_COND
from cida_attendance.utils import cleanup_dll, init_dll

logger = getLogger(__name__)


def check_server() -> bool:
    logger.info("Checking server...")
    config = load_config()
    client = HttpClient(auth_token=config["api_key"], url=config["url"])

    try:
        if data := client.get():
            last_sync = data.get("last_sync")
            logger.info("Last sync: %s %s", last_sync, data)
            return True
    except HttpClientError as e:
        logger.error("HTTP error: %s, %s", e, e.data, exc_info=e)

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

    client = HttpClient(auth_token=config["api_key"], url=config["url"])
    last_event_time = None

    try:
        if (data := client.get(device_serial=serial, device_model=model)) and (
            last_sync := data.get("last_sync")
        ):
            last_event_time = datetime.datetime.fromisoformat(last_sync)
    except HttpClientError as e:
        logger.error("HTTP error: %s", e)
        return False

    if last_event_time:
        start_date = last_event_time.astimezone(local_time.tzinfo) + datetime.timedelta(
            seconds=1
        )
    else:
        start_date = datetime.datetime(2000, 1, 1, tzinfo=local_time.tzinfo)

    device_data = {
        "device_id": serial,
        "device_model": model,
        "device_name": config["name"],
        "records": [],
    }

    def on_data(data):
        by_employee_no = (
            bytes(data.struAcsEventInfo.byEmployeeNo).decode("ascii").rstrip("\x00")
        )
        if by_employee_no:
            device_data["records"].append(
                {
                    "employee_id": by_employee_no,
                    "timestamp": data.struTime.to_python(local_time.tzinfo).isoformat(),
                    "event_type": data.struAcsEventInfo.byAttendanceStatus,
                    "event_minor": data.dwMinor,
                }
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

    try:
        response = client.post(device_data)
        logger.info("Server response: %s", response)
    except HttpClientError as e:
        logger.error("HTTP error: %s", e)
        return False

    logger.info("Events synchronized")
    return session.logout()


if __name__ == "__main__":
    synchronize()
