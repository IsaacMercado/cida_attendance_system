import logging
import sys
import time

from cida_attendance import sdk
from cida_attendance.config import load_config
from cida_attendance.sdk.session import Session, create_subscription_xml

# Configure logging to see what happens
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def main(duration_s: int | None = None) -> int:
    config = load_config()

    print("--- Manual Alarm Monitor ---")
    missing = set(("ip", "user", "password", "port")).difference(config)
    if missing:
        print(f"Missing credentials: {', '.join(missing)}")
        return 1

    with Session() as session:
        print(f"Connecting to {config.get('ip')}...")
        if not session.login(**config):
            print("❌ Login failed")
            return 1
        print("✅ Login successful")

        alarm_started = False

        def on_event(lCommand, pAlarmer, pAlarmInfo, pUser):
            if (int(lCommand) != int(sdk.COMM_ALARM_ACS)) or (
                pAlarmInfo.get("dwMajor") != sdk.MAJOR_EVENT
            ):
                return

            p_asc_event_info_extend = pAlarmInfo.get("pAcsEventInfoExtend", {})
            by_employee_no = p_asc_event_info_extend.get("byEmployeeNo")

            if not by_employee_no:
                logger.warning("Received event without employee number, skipping")
                return

            # fmt: off
            s_device_name = (
                pAlarmer.get("sDeviceName", b"").decode("ascii")
                or config.get("name", "Unknown")
            )
            # fmt: on
            s_serial_number = pAlarmer.get("sSerialNumber", "")

            s_time = pAlarmInfo.get("struTime")
            dw_minor = pAlarmInfo.get("dwMinor")
            by_attendance_status = p_asc_event_info_extend.get("byAttendanceStatus")

            record = {
                "device_name": s_device_name,
                "serial_number": s_serial_number,
                "employee_id": by_employee_no,
                "timestamp": s_time.isoformat(),
                "event_type": by_attendance_status,
                "event_minor": dw_minor,
            }

            print(
                f"🗒️  Event: {record['timestamp']} | Device: {record['device_name']} "
                f"({record['serial_number']}) | Employee: {record['employee_id']} "
                f"| Status: {record['event_type']} | Minor: {record['event_minor']}"
            )

        try:
            session.start_alarm_channel(
                subscribe_xml=create_subscription_xml(heartbeat_interval=5),
                by_level=1,
                by_alarm_info_type=1,
                on_event=on_event,
            )
            alarm_started = True

            print("📡 Listening for events... (Press Ctrl+C to stop)")

            if duration_s is None:
                while True:
                    time.sleep(1.0)
            else:
                end = time.monotonic() + float(duration_s)
                while time.monotonic() < end:
                    time.sleep(0.25)
        except RuntimeError as e:
            message = str(e)
            if "failed: 52" in message:
                print(
                    "❌ Could not open alarm channel: the device reached "
                    "the maximum active session limit (error 52).\n"
                    "Close active sessions on the device/client and try again."
                )
                return session.logout()
            raise
        except KeyboardInterrupt:
            print("\n🛑 Stopping...")
        finally:
            if alarm_started:
                session.stop_alarm_channel()
            session.logout()

    return 0


if __name__ == "__main__":
    if len(sys.argv) > 1:
        duration_s = sys.argv[1]
        try:
            duration_s = int(duration_s)
        except ValueError:
            print(f"Invalid duration: {duration_s}")
            sys.exit(1)
    else:
        duration_s = None
    sys.exit(main(duration_s))
