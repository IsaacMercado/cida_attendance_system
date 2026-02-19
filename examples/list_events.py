from cida_attendance.config import load_config
from cida_attendance.sdk.session import Session


def main() -> None:
    config = load_config()
    print("--- Query Today's Events ---")

    with Session() as session:
        print(f"Connecting to {config.get('ip')}...")
        if not session.login(**config):
            print("❌ Login failed")
            return 1
        print("✅ Login successful")

        now = session.get_device_time()
        start = now.replace(hour=0, minute=0, second=0, microsecond=0)

        print(f"Querying from: {start} to {now}")

        try:
            for detail in session.get_asc_event(
                dw_major=0x5,
                start_time=start,
                end_time=now,
                by_search_type=1,
                by_event_attribute=1,
            ):
                acs = detail.get("struAcsEventInfo") or {}
                employee = acs.get("byEmployeeNo")
                stru_time = detail.get("struTime")
                status = acs.get("byAttendanceStatus")
                minor = detail.get("dwMinor")

                print(
                    f"🕒 {stru_time} | Employee: {employee:<10} "
                    f"| Status: {status} | Minor: {minor}"
                )
            print("\nDownload completed.")
        except Exception as e:
            print("\n❌ Error during download:", e)

        session.logout()


if __name__ == "__main__":
    main()
