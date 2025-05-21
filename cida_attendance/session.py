import ctypes
import datetime
import re
from logging import getLogger
from typing import Callable
from xml.dom import minidom

from cida_attendance.structures import NET_DVR_DEVICEINFO_V40, NET_DVR_USER_LOGIN_INFO
from cida_attendance.utils import (
    NET_DVR_RemoteConfig,
    dll,
    get_last_error,
    net_dvr_xml_config,
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

    def login(self, **config):
        login_info = NET_DVR_USER_LOGIN_INFO.login(
            config["ip"].encode("ascii"),
            config["user"].encode("ascii"),
            config["password"].encode("ascii"),
            config["port"],
        )
        device_info = NET_DVR_DEVICEINFO_V40()
        user_id = dll.NET_DVR_Login_V40(
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
            dll.NET_DVR_Logout(self.user_id)
            self.user_id = None
        dll.NET_DVR_Cleanup()
        return True

    def send_data_request(
        self,
        url: str,
        in_buffer: str | None = None,
        recv_timeout: int | None = None,
    ) -> str:
        return net_dvr_xml_config(
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

    def run_remote_config(
        self,
        command: int,
        cond: ctypes.Structure,
        on_status: Callable = None,
        on_progress: Callable = None,
        on_data: Callable = None,
        data_cls: ctypes.Structure = None,
    ):
        NET_DVR_RemoteConfig(
            self.user_id,
            command,
            cond,
            on_status=on_status,
            on_progress=on_progress,
            on_data=on_data,
            data_cls=data_cls,
        )
