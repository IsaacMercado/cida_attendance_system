from __future__ import annotations

import argparse
import datetime as dt
import json

from cida_attendance.config import load_config
from cida_attendance.sdk.session import Session

DEFAULT_CEDULA = "5524282"
DEFAULT_FROM_DATE = "2026-05-17"
DEFAULT_TO_DATE = "2026-05-30"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Consulta eventos de asistencia de una cedula directamente "
            "desde el dispositivo"
        )
    )
    parser.add_argument(
        "--cedula",
        default=DEFAULT_CEDULA,
        help="Cedula a consultar",
    )
    parser.add_argument(
        "--from-date",
        default=DEFAULT_FROM_DATE,
        help="Fecha inicial en formato YYYY-MM-DD",
    )
    parser.add_argument(
        "--to-date",
        default=DEFAULT_TO_DATE,
        help="Fecha final en formato YYYY-MM-DD",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Imprime la salida completa en JSON",
    )
    return parser.parse_args()


def parse_date(date_str: str) -> dt.date:
    try:
        return dt.date.fromisoformat(date_str)
    except ValueError as exc:
        raise SystemExit(f"Fecha invalida: {date_str}. Usa YYYY-MM-DD") from exc


def build_range(
    from_date: dt.date, to_date: dt.date
) -> tuple[dt.datetime, dt.datetime]:
    if from_date > to_date:
        raise SystemExit("La fecha inicial no puede ser mayor que la fecha final")

    start_dt = dt.datetime.combine(from_date, dt.time.min)
    end_dt = dt.datetime.combine(to_date, dt.time.max.replace(microsecond=0))
    return start_dt, end_dt


def main() -> int:
    args = parse_args()
    from_date = parse_date(args.from_date)
    to_date = parse_date(args.to_date)
    start_dt, end_dt = build_range(from_date, to_date)

    config = load_config()

    with Session() as session:
        if not session.login(**config):
            print("No se pudo iniciar sesion en el dispositivo")
            return 1

        device_time = session.get_device_time()
        tz = device_time.tzinfo
        if tz is not None:
            start_dt = start_dt.replace(tzinfo=tz)
            end_dt = end_dt.replace(tzinfo=tz)

        events = []
        for detail in session.get_asc_event(
            dw_major=0x5,
            start_time=start_dt,
            end_time=end_dt,
            by_search_type=1,
            by_event_attribute=1,
            by_employee_no=args.cedula,
        ):
            acs = detail.get("struAcsEventInfo") or {}
            stru_time = detail.get("struTime")
            if isinstance(stru_time, dt.datetime) and tz is not None:
                stru_time = stru_time.replace(tzinfo=tz)

            events.append(
                {
                    "employee_id": acs.get("byEmployeeNo"),
                    "timestamp": stru_time.isoformat()
                    if isinstance(stru_time, dt.datetime)
                    else str(stru_time),
                    "event_type": acs.get("byAttendanceStatus"),
                    "event_minor": detail.get("dwMinor"),
                }
            )

        session.logout()

    if args.json:
        print(
            json.dumps(
                {
                    "cedula": args.cedula,
                    "from_date": args.from_date,
                    "to_date": args.to_date,
                    "total": len(events),
                    "records": events,
                },
                ensure_ascii=True,
                indent=2,
            )
        )
        return 0

    print(f"Cedula: {args.cedula}")
    print(f"Rango: {args.from_date} a {args.to_date}")
    print(f"Total de registros: {len(events)}")

    if not events:
        return 0

    print("\nRegistros:")
    for event in events:
        print(
            "- {timestamp} | employee_id={employee_id} | event_type={event_type} | "
            "event_minor={event_minor}".format(**event)
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
