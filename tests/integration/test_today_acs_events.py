import sys
from pathlib import Path
from typing import Any

from cida_attendance.config import load_config
from cida_attendance.sdk.session import Session
from cida_attendance.sdk.utils import ctypes_to_dict


def main() -> None:
    config = load_config()

    with Session() as session:
        if not session.login(**config):
            print("Login falló", file=sys.stderr)
            return 1

        now, tz = session.get_device_time()
        start = now.replace(hour=0, minute=0, second=0, microsecond=0)

        try:
            out: list[dict[str, Any]] = []

            def _on_data(detail: Any) -> None:
                if len(out) >= 20:
                    return
                out.append(ctypes_to_dict(detail, tz=tz))

            session.async_get_asc_event(
                start,
                now,
                _on_data,
                major=0x5,
            )

            for ev in out:
                stru_time = ev.get("struTime")
                acs = ev.get("struAcsEventInfo") or {}
                employee = acs.get("byEmployeeNo")
                if isinstance(employee, (bytes, bytearray)):
                    employee = employee.split(b"\x00", 1)[0].decode(
                        "ascii", errors="replace"
                    )
                status = acs.get("byAttendanceStatus")
                print(
                    f"time={stru_time} employee={employee!r} status={status} minor={ev.get('dwMinor')}"
                )

            print(f"total={len(out)}")

        finally:
            session.logout()


if __name__ == "__main__":
    main()
