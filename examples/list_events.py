from cida_attendance.config import load_config
from cida_attendance.sdk.session import Session
from cida_attendance.sdk.utils import bytes_to_str, ctypes_to_dict


def main() -> None:
    config = load_config()
    print("--- Query Today's Events ---")

    with Session() as session:
        print(f"Connecting to {config.get('ip')}...")
        if not session.login(**config):
            print("❌ Login failed")
            return 1
        print("✅ Login successful")

        now, _tz = session.get_device_time()
        start = now.replace(hour=0, minute=0, second=0, microsecond=0)

        print(f"Querying from: {start} to {now}")

        def _on_data_progress(detail):
            ev = ctypes_to_dict(detail)

            acs = ev.get("struAcsEventInfo") or {}
            employee = bytes_to_str(acs.get("byEmployeeNo"))
            stru_time = ev.get("struTime")
            status = acs.get("byAttendanceStatus")
            minor = ev.get("dwMinor")

            print(
                f"🕒 {stru_time} | Employee: {employee:<10} "
                f"| Status: {status} | Minor: {minor}"
            )

        try:
            session.get_asc_event(
                on_data=_on_data_progress,
                dw_major=0x5,
                start_time=start,
                end_time=now,
                by_search_type=1,
                by_event_attribute=1,
            )
            print("\nDownload completed.")
        except Exception as e:
            print("\n❌ Error during download:", e)

        session.logout()


if __name__ == "__main__":
    main()
