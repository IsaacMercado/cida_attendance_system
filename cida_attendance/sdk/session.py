import ctypes
import datetime
import re
import time
from logging import getLogger
from typing import Any, Callable
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
from cida_attendance.sdk.utils import ctypes_to_dict

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
        self._alarm_handle: int | None = None
        self._alarm_callbacks: dict[int, Any] = {}
        self._alarm_subscribe_buf: ctypes.Array[ctypes.c_char] | None = None

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
        if self._alarm_handle is not None:
            self.stop_alarm_channel()

        if self.user_id is not None and self.user_id >= 0:
            sdk.NET_DVR_Logout(self.user_id)
            self.user_id = None
        sdk.NET_DVR_Cleanup()
        return True

    @staticmethod
    def build_subscribe_all_events_xml() -> str:
        return (
            '<SubscribeEvent version="2.0" xmlns="http://www.isapi.org/ver20/XMLSchema">\r\n'
            "<eventMode>all</eventMode>\r\n"
            "</SubscribeEvent>\r\n"
        )

    def start_alarm_channel(
        self,
        *,
        subscribe_xml: str | None = None,
        callback_index: int = 0,
        on_event: Callable[[int, dict[str, Any] | None, Any, int | None], None]
        | None = None,
        tz: datetime.tzinfo | None = None,
        # NET_DVR_SETUPALARM_PARAM_V50
        by_level: int | None = None,
        by_alarm_info_type: int | None = None,
        by_ret_alarm_type_v40: int | None = None,
        by_ret_dev_info_version: int | None = None,
        by_ret_vqd_alarm_type: int | None = None,
        by_face_alarm_detection: int | None = None,
        by_support: int | None = None,
        by_broken_net_http: int | None = None,
        w_task_no: int | None = None,
        by_deploy_type: int | None = None,
        by_sub_scription: int | None = None,
        by_broken_net_http_v60: int | None = None,
        by_alarm_type_url: int | None = None,
        by_custom_ctrl: int | None = None,
    ) -> int:
        if self.user_id is None:
            raise RuntimeError("Debe iniciar sesión antes de armar el canal de alarmas")

        if tz is None:
            try:
                _local_time, tz = self.get_device_time()
            except Exception:
                tz = None

        def _callback(
            lCommand: int,
            pAlarmer: Any,
            pAlarmInfo: Any,
            dwBufLen: int,
            pUser: Any,
        ) -> None:
            try:
                alarm_info_ptr: ctypes.c_void_p | None = None
                if pAlarmInfo:
                    try:
                        alarm_info_ptr = ctypes.cast(pAlarmInfo, ctypes.c_void_p)
                    except Exception:
                        alarm_info_ptr = ctypes.c_void_p(int(pAlarmInfo))

                alarmer_dict: dict[str, Any] | None = None
                if pAlarmer:
                    try:
                        alarmer_dict = ctypes_to_dict(pAlarmer.contents, tz=tz)
                    except Exception:
                        alarmer_dict = None

                p_user_ptr: int | None = None
                if pUser:
                    try:
                        p_user_ptr = int(ctypes.cast(pUser, ctypes.c_void_p).value)
                    except Exception:
                        p_user_ptr = None

                alarm_info: Any = None
                if alarm_info_ptr and alarm_info_ptr.value and int(dwBufLen) > 0:
                    if int(lCommand) == sdk.COMM_ISAPI_ALARM:
                        if int(dwBufLen) >= ctypes.sizeof(sdk.NET_DVR_ALARM_ISAPI_INFO):
                            isapi_info = ctypes.cast(
                                alarm_info_ptr,
                                sdk.LPNET_DVR_ALARM_ISAPI_INFO,
                            ).contents
                            alarm_info = ctypes_to_dict(isapi_info, tz=tz)
                        else:
                            alarm_info = ctypes.string_at(alarm_info_ptr, int(dwBufLen))
                    elif int(lCommand) == sdk.COMM_ALARM_ACS:
                        if int(dwBufLen) >= ctypes.sizeof(sdk.NET_DVR_ACS_ALARM_INFO):
                            acs_info = ctypes.cast(
                                alarm_info_ptr,
                                sdk.LPNET_DVR_ACS_ALARM_INFO,
                            ).contents
                            alarm_info = ctypes_to_dict(acs_info, tz=tz)
                        else:
                            alarm_info = ctypes.string_at(alarm_info_ptr, int(dwBufLen))
                    else:
                        alarm_info = ctypes.string_at(alarm_info_ptr, int(dwBufLen))

                if on_event:
                    on_event(
                        int(lCommand),
                        alarmer_dict,
                        alarm_info,
                        p_user_ptr,
                    )
                else:
                    logger.info(
                        "Alarm/event: cmd=%s len=%s alarmer=%s",
                        int(lCommand),
                        int(dwBufLen),
                        bool(alarmer_dict),
                    )
            except Exception:
                logger.exception("Error procesando callback de alarma/evento")

        callback = sdk.MSGCallBack(_callback)
        self._alarm_callbacks[int(callback_index)] = callback

        ok = sdk.NET_DVR_SetDVRMessageCallBack_V50(int(callback_index), callback, None)
        if not ok:
            code, msg = get_last_error()
            raise RuntimeError(f"NET_DVR_SetDVRMessageCallBack_V50 falló: {code} {msg}")

        setup = sdk.NET_DVR_SETUPALARM_PARAM_V50()
        setup.dwSize = ctypes.sizeof(setup)

        if by_level is not None:
            setup.byLevel = int(by_level)
        if by_alarm_info_type is not None:
            setup.byAlarmInfoType = int(by_alarm_info_type)
        if by_ret_alarm_type_v40 is not None:
            setup.byRetAlarmTypeV40 = int(by_ret_alarm_type_v40)
        if by_ret_dev_info_version is not None:
            setup.byRetDevInfoVersion = int(by_ret_dev_info_version)
        if by_ret_vqd_alarm_type is not None:
            setup.byRetVQDAlarmType = int(by_ret_vqd_alarm_type)
        if by_face_alarm_detection is not None:
            setup.byFaceAlarmDetection = int(by_face_alarm_detection)
        if by_support is not None:
            setup.bySupport = int(by_support)
        if by_broken_net_http is not None:
            setup.byBrokenNetHttp = int(by_broken_net_http)
        if w_task_no is not None:
            setup.wTaskNo = int(w_task_no)
        if by_deploy_type is not None:
            setup.byDeployType = int(by_deploy_type)
        if by_broken_net_http_v60 is not None:
            setup.byBrokenNetHttpV60 = int(by_broken_net_http_v60)
        if by_alarm_type_url is not None:
            setup.byAlarmTypeURL = int(by_alarm_type_url)
        if by_custom_ctrl is not None:
            setup.byCustomCtrl = int(by_custom_ctrl)

        sub_ptr = None
        sub_len = 0
        if subscribe_xml:
            sub_bytes = subscribe_xml.encode("utf-8")
            self._alarm_subscribe_buf = ctypes.create_string_buffer(sub_bytes)
            sub_ptr = self._alarm_subscribe_buf
            sub_len = len(sub_bytes)
        else:
            self._alarm_subscribe_buf = None

        if by_sub_scription is not None:
            setup.bySubScription = int(by_sub_scription)
            if int(setup.bySubScription) == 1 and not subscribe_xml:
                raise ValueError(
                    "by_sub_scription=1 requiere subscribe_xml (no se entregó)."
                )
        elif subscribe_xml:
            setup.bySubScription = 1

        handle = sdk.NET_DVR_SetupAlarmChan_V50(
            int(self.user_id),
            ctypes.byref(setup),
            sub_ptr,
            int(sub_len),
        )

        if handle < 0:
            code, msg = get_last_error()
            raise RuntimeError(f"NET_DVR_SetupAlarmChan_V50 falló: {code} {msg}")

        self._alarm_handle = int(handle)
        return int(handle)

    def stop_alarm_channel(self) -> None:
        if self._alarm_handle is None:
            return

        handle = int(self._alarm_handle)
        self._alarm_handle = None

        ok = sdk.NET_DVR_CloseAlarmChan_V30(handle)
        if not ok:
            logger.warning("NET_DVR_CloseAlarmChan_V30 falló: %s", get_last_error())

    def listen_alarm_events(self, duration_s: float | None = None) -> None:
        if self._alarm_handle is None:
            raise RuntimeError(
                "No hay canal de alarmas armado. Llama a start_alarm_channel()."
            )

        if duration_s is None:
            while True:
                time.sleep(1.0)
        else:
            end = time.monotonic() + float(duration_s)
            while time.monotonic() < end:
                time.sleep(0.25)

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

        # `localTime` es tiempo local del dispositivo; lo hacemos timezone-aware
        # con el offset entregado por `timeZone`.
        return datetime.datetime.fromisoformat(slt).replace(tzinfo=tz), tz

    def async_get_asc_event(
        self,
        start_date: datetime.datetime,
        local_time: datetime.datetime,
        on_data: Callable | None = None,
        *,
        major: int | None = 0x5,
        minor: int | None = None,
        on_status: Callable | None = None,
        on_progress: Callable | None = None,
        timeout_s: float | None = 15.0,
    ) -> None:
        build_net_dvr_remoteconfig(
            self.user_id,
            sdk.NET_DVR_GET_ACS_EVENT,
            build_net_dvr_acs_event_cond(
                major=major,
                minor=minor,
                start_time=start_date,
                end_time=local_time,
            ),
            on_status=on_status,
            on_progress=on_progress,
            on_data=on_data,
            data_cls=sdk.NET_DVR_ACS_EVENT_CFG,
            timeout_s=timeout_s,
        )
