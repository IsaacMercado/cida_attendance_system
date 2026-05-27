from urllib.parse import urlencode
from urllib.request import urlopen
from zoneinfo import ZoneInfo
import json
import datetime

DEFAULT_TIMEZONE_STRING = "America/Caracas"
DEFAULT_TIMEZONE = ZoneInfo(DEFAULT_TIMEZONE_STRING)


def get_current_datetime_from_timeapi(timeout: float = 1.0) -> datetime.datetime | None:
    api_url_param = {"timezone": DEFAULT_TIMEZONE_STRING}
    api_url = f"https://timeapi.io/api/v1/time/current/zone?{urlencode(api_url_param)}"

    try:
        with urlopen(api_url, timeout=timeout) as response:
            if response.status == 200:
                data = json.loads(response.read())
                datetime_str = data.get("date_time")
                if datetime_str:
                    return datetime.datetime.fromisoformat(datetime_str).replace(
                        tzinfo=DEFAULT_TIMEZONE
                    )
    except OSError:
        pass

    return None


def get_current_datetime(try_timeapi: bool = True) -> datetime.datetime:
    if try_timeapi:
        dt = get_current_datetime_from_timeapi()
        if dt is not None:
            return dt
    return datetime.datetime.now(DEFAULT_TIMEZONE)
