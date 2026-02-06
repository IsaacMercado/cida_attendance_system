import ctypes
import datetime
import re
from logging import getLogger
from typing import Callable
from xml.dom import minidom

from cida_attendance import sdk
from cida_attendance.sdk.bindings import (
    build_net_dvr_acs_event_cond,
    build_net_dvr_remoteconfig,
    build_net_dvr_user_login_info,
    build_net_dvr_xml_config_input,
    cleanup_dll,
    get_last_error,
    init_dll,
)

logger = getLogger(__name__)


def get_values_from_xml(xml: str, tags: list[str]):
    dom = minidom.parseString(xml)
    for tag in tags:
        elements = dom.getElementsByTagName(tag)
        if elements:
            for element in elements:
                if element.firstChild:
                    yield element.firstChild.nodeValue


class Session:
    def __init__(self):
        self.user_id = None

    def __del__(self):
        self.logout()

    def init(self):
        init_dll()

    def cleanup(self):
        cleanup_dll()

    def __enter__(self):
        self.init()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.cleanup()

    def login(self, **config):
        login_info = build_net_dvr_user_login_info(
            config["ip"].encode("ascii"),
            config["user"].encode("ascii"),
            config["password"].encode("ascii"),
            config["port"],
        )
        device_info = sdk.NET_DVR_DEVICEINFO_V40()
        user_id = sdk.NET_DVR_Login_V40(
            ctypes.byref(login_info),
            ctypes.byref(device_info),
        )

        logger.info("User ID: %s", user_id)

        if user_id < 0:
            logger.error(
                "Error code: %d, %s",
                *get_last_error(),
            )
            return False

        self.user_id = user_id
        return True

    def logout(self):
        if self.user_id:
            sdk.NET_DVR_Logout(self.user_id)
            self.user_id = None
        sdk.NET_DVR_Cleanup()
        return True

    def send_data_request(
        self,
        url: str,
        in_buffer: str | None = None,
        recv_timeout: int | None = None,
    ) -> str:
        return build_net_dvr_xml_config_input(
            self.user_id,
            url,
            in_buffer,
            recv_timeout,
        ).decode("ascii")

    def get_device_info(self):
        return get_values_from_xml(
            self.send_data_request("GET /ISAPI/System/deviceInfo"),
            ["model", "serialNumber"],
        )

    def get_device_time(self):
        slt, stz = get_values_from_xml(
            self.send_data_request("GET /ISAPI/System/time"),
            ["localTime", "timeZone"],
        )

        mtz = re.match(r"([A-Z]+)([-+]\d+):(\d+):(\d+)", stz)

        if mtz:
            gtz = mtz.groups()
            tz = datetime.timezone(
                datetime.timedelta(
                    hours=int(gtz[1]),
                    minutes=int(gtz[2]),
                    seconds=int(gtz[3]),
                ),
                name=gtz[0],
            )
        else:
            tz = datetime.timezone.utc

        return datetime.datetime.fromisoformat(slt), tz

    def async_get_asc_event(
        self,
        start_date: datetime.datetime,
        local_time: datetime.datetime,
        major: int = None,
        minor: int = None,
        on_data: Callable = None,
        on_status: Callable = None,
        on_progress: Callable = None,
        timeout_s: float | None = 15.0,
    ):
        build_net_dvr_remoteconfig(
            self.user_id,
            sdk.NET_DVR_GET_ACS_EVENT,
            build_net_dvr_acs_event_cond(
                major=0x5,
                # minor=0x26,
                # minor=0x01,
                start_time=start_date,
                end_time=local_time,
            ),
            on_status=on_status,
            on_progress=on_progress,
            on_data=on_data,
            data_cls=sdk.NET_DVR_ACS_EVENT_CFG,
            timeout_s=timeout_s,
        )
