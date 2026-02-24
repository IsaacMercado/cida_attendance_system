import datetime
import time
from logging import getLogger

from cida_attendance.config import load_config
from cida_attendance.core.client import HttpClient, HttpClientError
from cida_attendance.sdk.api.macros import COMM_ALARM_ACS, MAJOR_EVENT
from cida_attendance.sdk.session import Session, create_subscription_xml

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


def synchronize_live(duration_s: int | None = None, wait: float = 0.5) -> int:
    config = load_config()

    with Session() as session:
        if not session.login(**config):
            return False

        model, serial = session.get_device_info()
        logger.info("Device model: %s", model)

        client = HttpClient(auth_token=config["api_key"], url=config["url"])
        device_data = {
            "device_id": serial,
            "device_model": model,
            "device_name": config["name"],
            "records": [],
        }

        alarm_started = False

        def on_event(lCommand, pAlarmer, pAlarmInfo, pUser):
            if (int(lCommand) != COMM_ALARM_ACS) or (
                pAlarmInfo.get("dwMajor") != MAJOR_EVENT
            ):
                return

            p_asc_event_info_extend = pAlarmInfo.get("pAcsEventInfoExtend", {})
            by_employee_no = p_asc_event_info_extend.get("byEmployeeNo")

            if not by_employee_no:
                logger.warning("Received event without employee number, skipping")
                return

            s_time = pAlarmInfo.get("struTime")
            dw_minor = pAlarmInfo.get("dwMinor")
            by_attendance_status = p_asc_event_info_extend.get("byAttendanceStatus")

            record = {
                "employee_id": by_employee_no,
                "timestamp": s_time.isoformat(),
                "event_type": by_attendance_status,
                "event_minor": dw_minor,
            }
            device_data["records"].append(record)

        def send_records():
            if not device_data["records"]:
                return

            try:
                response = client.post(device_data)
                logger.info("Server response: %s", response)
                device_data["records"].clear()
            except HttpClientError as e:
                logger.error("HTTP error: %s", e)

        try:
            session.start_alarm_channel(
                subscribe_xml=create_subscription_xml(heartbeat_interval=5),
                by_level=1,
                by_alarm_info_type=1,
                on_event=on_event,
            )
            alarm_started = True

            logger.info("📡 Listening for events... (Press Ctrl+C to stop)")

            if duration_s is None:
                while True:
                    send_records()
                    time.sleep(wait)
            else:
                end = time.monotonic() + float(duration_s)
                while time.monotonic() < end:
                    send_records()
                    time.sleep(wait)

        except RuntimeError as error:
            message = str(error)
            if "failed: 52" in message:
                logger.error(
                    "❌ Could not open alarm channel: the device reached "
                    "the maximum active session limit (error 52). "
                    "Close active sessions on the device/client and try again.",
                    exc_info=error,
                )
                return session.logout()
            raise
        except KeyboardInterrupt:
            logger.info("🛑 Stopping...")
        finally:
            if alarm_started:
                session.stop_alarm_channel()
            session.logout()

    return True


if __name__ == "__main__":
    synchronize()
