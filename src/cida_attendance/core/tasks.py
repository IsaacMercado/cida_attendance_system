import datetime
from logging import getLogger

from cida_attendance.config import load_config
from cida_attendance.core.client import HttpClient, HttpClientError
from cida_attendance.sdk.session import Session

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

    with Session() as session:
        if not session.login(**config):
            return False

    logger.info("Device checked")
    return session.logout()


def synchronize():
    logger.info("Synchronizing...")
    config = load_config()

    with Session() as session:
        if not session.login(**config):
            return False

        model, serial = session.get_device_info()
        local_time = session.get_device_time()
        tz = local_time.tzinfo

        logger.info("Device model: %s", model)

        client = HttpClient(auth_token=config["api_key"], url=config["url"])
        start_date = None

        try:
            if (data := client.get(device_serial=serial, device_model=model)) and (
                last_sync := data.get("last_sync")
            ):
                start_date = datetime.datetime.fromisoformat(
                    last_sync,
                ).replace(tzinfo=tz) + datetime.timedelta(seconds=1)
        except HttpClientError as e:
            logger.error("HTTP error: %s", e)
            return False

        start_date = start_date or datetime.datetime(2026, 2, 1, tzinfo=tz)

        if start_date > local_time:
            session.logout()
            return False

        device_data = {
            "device_id": serial,
            "device_model": model,
            "device_name": config["name"],
            "records": [],
        }

        for detail in session.get_asc_event(
            dw_major=0x5,
            start_time=start_date,
            end_time=local_time,
            by_search_type=1,
            by_event_attribute=1,
        ):
            acs = detail.get("struAcsEventInfo") or {}
            stru_time = detail.get("struTime").replace(tzinfo=tz).isoformat()
            record = {
                "employee_id": acs.get("byEmployeeNo"),
                "timestamp": stru_time,
                "event_type": acs.get("byAttendanceStatus"),
                "event_minor": detail.get("dwMinor"),
            }
            device_data["records"].append(record)

    if device_data["records"]:
        try:
            response = client.post(device_data)
            logger.info("Server response: %s", response)
        except HttpClientError as e:
            logger.error("HTTP error: %s", e)
            return session.logout()

    logger.info("Events synchronized")
    return session.logout()


if __name__ == "__main__":
    synchronize()
