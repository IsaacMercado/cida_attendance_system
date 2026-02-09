import json
import sys
from pathlib import Path

from cida_attendance.config import load_config
from cida_attendance.sdk.session import Session


def main() -> int:
    config = load_config()

    missing = [k for k in ("ip", "user", "password", "port") if not config.get(k)]
    if missing:
        print(
            "Config incompleta. Faltan: " + ", ".join(missing) + ".\n"
            "Config file: ~/.config/cida_attendance/config.ini (o CONFIG_FILE).",
            file=sys.stderr,
        )
        return 2

    def on_event(
        lCommand: int,
        pAlarmer: dict | None,
        pAlarmInfo: object,
        pUser: int | None,
    ) -> None:
        payload = {
            "lCommand": lCommand,
            "pUser": pUser,
            "pAlarmer": pAlarmer,
            "pAlarmInfo": pAlarmInfo,
        }
        print(json.dumps(payload, ensure_ascii=False, indent=2, default=str), flush=True)

    with Session() as session:
        if not session.login(**config):
            print("Login falló", file=sys.stderr)
            return 1

        session.start_alarm_channel(
            subscribe_xml=Session.build_subscribe_all_events_xml(),
            by_level=1,
            by_alarm_info_type=1,
            on_event=on_event,
        )

        print("Escuchando eventos... (Ctrl+C para salir)", flush=True)
        try:
            session.listen_alarm_events(duration_s=None)
        except KeyboardInterrupt:
            print("\nSaliendo...", flush=True)
        finally:
            session.stop_alarm_channel()
            session.logout()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
