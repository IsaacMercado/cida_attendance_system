from cida_attendance.config import load_config
from cida_attendance.sdk.session import Session
from cida_attendance.sdk.utils import ctypes_to_dict


def main() -> None:
    config = load_config()
    print("--- Query Today's Events ---")

    with Session() as session:
        print(f"Connecting to {config.get('ip')}...")
        if not session.login(**config):
            print("❌ Login failed")
            return 1
        print("✅ Login successful")

        now, tz = session.get_device_time()
        start = now.replace(hour=0, minute=0, second=0, microsecond=0)
        
        print(f"Querying from: {start} to {now}")

        out = []
        
        # Callback to see progress
        def _on_data_progress(detail):
            data = ctypes_to_dict(detail, tz=tz)
            out.append(data)
            print(f"received: {data.get('struTime')} (Total: {len(out)})", end="\r")

        try:
            session.async_get_asc_event(
                start,
                now,
                _on_data_progress,
                major=0x5,
            )
            print("\nDownload completed.")
        except Exception as e:
            print("\n❌ Error during download:", e)

        print("\n--- Results ---")
        for ev in out:
            stru_time = ev.get("struTime")
            acs = ev.get("struAcsEventInfo") or {}
            
            # Decode employee ID
            employee = acs.get("byEmployeeNo")
            if isinstance(employee, (bytes, bytearray)):
                employee = employee.split(b"\x00", 1)[0].decode("ascii", errors="replace")
                
            status = acs.get("byAttendanceStatus")
            minor = ev.get("dwMinor")
            print(f"🕒 {stru_time} | Employee: {employee:<10} | Status: {status} | Minor: {minor}")

        print(f"Total events: {len(out)}")

if __name__ == "__main__":
    main()
