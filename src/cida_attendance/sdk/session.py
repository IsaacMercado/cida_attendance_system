import ctypes
import dataclasses
import datetime
import re
import threading
import time
from logging import getLogger
from typing import Any, Callable, Literal
from xml.dom import minidom

from cida_attendance import sdk
from cida_attendance.sdk.bindings import (
    build_fremoteconfigcallback,
    build_net_dvr_acs_event_cond,
    build_net_dvr_setupalarm_param_v50,
    build_net_dvr_user_login_info,
    build_net_dvr_xml_config_input,
    build_net_dvr_xml_config_output,
    get_last_error,
    run_net_dvr_startremoteconfig,
    run_net_dvr_stdxmlconfig,
)
from cida_attendance.sdk.utils import ctypes_to_dict

logger = getLogger(__name__)


@dataclasses.dataclass
class XMLSubscribeEvent:
    """
    Represents an event subscription filter for ISAPI alarm/event subscription.

    Attributes:
        type (str): Alarm/event types, which are obtained from the capability, refer to Alarm/Event Types for Subscription for its values.
        minor_alarm (list[int] | None): Minor alarm type: "0x400,0x401,0x402,0x403". This node is required when type is "AccessControllerEvent".
        minor_exception (list[int] | None): Minor exception type: "0x400,0x401,0x402,0x403". This node is required when type is "AccessControllerEvent".
        minor_operation (list[int] | None): Minor operation type: "0x400,0x401,0x402,0x403". This node is required when type is "AccessControllerEvent".
        minor_event (list[int] | None): Minor event type: "0x01,0x02,0x03,0x04". This node is required when type is "AccessControllerEvent".
        picture_url_type (Literal["binary", "localURL", "cloudStorageURL"] | None): Alarm picture format: "binary"-binary, "localURL"-device local URL, "cloudStorageURL"-cloud storage URL.
    """

    type: str
    minor_alarm: list[int] | None = None
    minor_exception: list[int] | None = None
    minor_operation: list[int] | None = None
    minor_event: list[int] | None = None
    picture_url_type: Literal["binary", "localURL", "cloudStorageURL"] | None = None

    def to_dom(self, dom: minidom.Document | None = None) -> minidom.Element:
        dom = dom or minidom.Document()
        event = dom.createElement("Event")

        def list_to_hex_string(values: list[int]) -> str:
            return ",".join(f"0x{v:02x}" for v in values)

        def create_text_element(name: str, text: str) -> minidom.Element:
            el = dom.createElement(name)
            el.appendChild(dom.createTextNode(text))
            event.appendChild(el)
            return el

        create_text_element("type", self.type)

        if self.type == "AccessControllerEvent" and not all(
            (
                self.minor_alarm,
                self.minor_exception,
                self.minor_operation,
                self.minor_event,
            )
        ):
            raise ValueError(
                "type=AccessControllerEvent require all of "
                "minor_alarm, minor_exception, minor_operation, minor_event."
            )

        if self.minor_alarm is not None:
            create_text_element(
                "minorAlarm",
                list_to_hex_string(self.minor_alarm),
            )

        if self.minor_exception is not None:
            create_text_element(
                "minorException",
                list_to_hex_string(self.minor_exception),
            )

        if self.minor_operation is not None:
            create_text_element(
                "minorOperation",
                list_to_hex_string(self.minor_operation),
            )

        if self.minor_event is not None:
            create_text_element(
                "minorEvent",
                list_to_hex_string(self.minor_event),
            )

        if self.picture_url_type is not None:
            create_text_element("pictureURLType", self.picture_url_type)

        return event


def create_subscription_xml(
    event_mode: Literal["all", "list"] = "all",
    heartbeat_interval: int | None = None,
    event_list: list[XMLSubscribeEvent] | None = None,
    channels: list[int] | None = None,
    identity_key: str | None = None,
) -> str:
    """
    Create XML string for ISAPI alarm/event subscription.
    Args:
        event_mode: "all" to subscribe to all events, "list" to subscribe to specific events defined in event_list.
        heartbeat_interval: Optional heartbeat interval in seconds. If not provided, the device default will be used.
        event_list: List of XMLSubscribeEvent objects defining specific events to subscribe to (required if event_mode is "list").
        channels: Optional list of channel numbers to arm (e.g., [1, 2, 3]). If not provided, all channels will be armed.
        identity_key: Optional string (max 64 chars) for subscription interaction command, used for subscribing to comparison results of face picture library.
    """

    dom = minidom.Document()
    subscribe_event = dom.createElement("SubscribeEvent")
    subscribe_event.setAttribute("version", "2.0")
    subscribe_event.setAttribute("xmlns", "http://www.isapi.org/ver20/XMLSchema")
    dom.appendChild(subscribe_event)

    if heartbeat_interval is not None:
        heartbeat = dom.createElement("heartbeat")
        heartbeat.appendChild(dom.createTextNode(str(heartbeat_interval)))
        subscribe_event.appendChild(heartbeat)

    _event_mode = dom.createElement("eventMode")
    _event_mode.appendChild(dom.createTextNode(event_mode))
    subscribe_event.appendChild(_event_mode)

    if event_mode == "list":
        if not event_list:
            raise ValueError("event_mode=list requires a non-empty event_list")

        event_list_el = dom.createElement("EventList")
        subscribe_event.appendChild(event_list_el)

        for event in event_list:
            event_el = event.to_dom(dom)
            event_list_el.appendChild(event_el)

    if channels:
        channels_el = dom.createElement("channels")
        subscribe_event.appendChild(channels_el)
        channels_el.appendChild(dom.createTextNode(",".join(str(c) for c in channels)))

    if identity_key:
        identity_key_el = dom.createElement("identityKey")
        identity_key_el.setAttribute("max", "64")
        identity_key_el.appendChild(dom.createTextNode(identity_key))
        subscribe_event.appendChild(identity_key_el)

    return dom.documentElement.toprettyxml(indent="  ").strip()


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

    def init(self):
        sdk.NET_DVR_Init()
        sdk.NET_DVR_SetConnectTime(2000, 1)
        sdk.NET_DVR_SetReconnect(10000, True)

    def cleanup(self):
        sdk.NET_DVR_Cleanup()

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

        return True

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
            if by_sub_scription == 1 and not subscribe_xml:
                raise ValueError(
                    "by_sub_scription=1 requiere subscribe_xml (no se entregó)."
                )
        elif subscribe_xml:
            by_sub_scription = 1

        setup = build_net_dvr_setupalarm_param_v50(
            by_level,
            by_alarm_info_type,
            by_ret_alarm_type_v40,
            by_ret_dev_info_version,
            by_ret_vqd_alarm_type,
            by_face_alarm_detection,
            by_support,
            by_broken_net_http,
            w_task_no,
            by_deploy_type,
            by_sub_scription,
            by_broken_net_http_v60,
            by_alarm_type_url,
            by_custom_ctrl,
        )

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

    def request_stdxmlconfig(
        self,
        url: str,
        in_buffer: str | None = None,
        recv_timeout: int | None = None,
    ) -> str:
        xml_config_input = build_net_dvr_xml_config_input(
            url,
            in_buffer,
            recv_timeout,
        )
        xml_config_output = build_net_dvr_xml_config_output()

        run_net_dvr_stdxmlconfig(
            self.user_id,
            xml_config_input,
            xml_config_output,
        )

        xml_size = int(xml_config_output.dwReturnedXMLSize)
        if xml_size > 0:
            payload = ctypes.string_at(xml_config_output.lpOutBuffer, xml_size)
        else:
            payload = ctypes.string_at(xml_config_output.lpOutBuffer)

        return payload.decode("ascii")

    def get_device_info(self):
        return get_values_from_xml(
            self.request_stdxmlconfig("GET /ISAPI/System/deviceInfo"),
            ["model", "serialNumber"],
        )

    def get_device_time(self):
        slt, stz = get_values_from_xml(
            self.request_stdxmlconfig("GET /ISAPI/System/time"),
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

    def aget_asc_event(
        self,
        on_data: Callable | None = None,
        on_status: Callable | None = None,
        on_progress: Callable | None = None,
        timeout_s: float | None = 15.0,
        # Conditions for filtering access control events:
        dw_major: int | None = None,
        dw_minor: int | None = None,
        start_time: datetime.datetime | None = None,
        end_time: datetime.datetime | None = None,
        by_card_no: str | None = None,
        by_name: str | None = None,
        by_pic_enable: Literal[0, 1] | None = None,
        by_time_type: Literal[0, 1] | None = None,
        dw_begin_serial_no: int | None = None,
        dw_end_serial_no: int | None = None,
        dw_iot_channel_no: int | None = None,
        w_inductive_event_type: int | None = None,
        by_search_type: Literal[0, 1, 2] | None = None,
        by_event_attribute: Literal[0, 1, 2] | None = None,
        sz_monitor_id: str | None = None,
        by_employee_no: str | None = None,
    ) -> None:
        assert any(v is not None for v in (on_data, on_status, on_progress)), (
            "At least one callback (on_data, on_status, on_progress) must be provided."
        )

        _cond = build_net_dvr_acs_event_cond(
            dw_major=dw_major,
            dw_minor=dw_minor,
            start_time=start_time,
            end_time=end_time,
            by_card_no=by_card_no,
            by_name=by_name,
            by_pic_enable=by_pic_enable,
            by_time_type=by_time_type,
            dw_begin_serial_no=dw_begin_serial_no,
            dw_end_serial_no=dw_end_serial_no,
            dw_iot_channel_no=dw_iot_channel_no,
            w_inductive_event_type=w_inductive_event_type,
            by_search_type=by_search_type,
            by_event_attribute=by_event_attribute,
            sz_monitor_id=sz_monitor_id,
            by_employee_no=by_employee_no,
        )

        _event = threading.Event()

        def _callback(dw_type, data):
            if dw_type == sdk.NET_SDK_CALLBACK_TYPE_STATUS:
                if on_status:
                    on_status(*data)
                _event.set()
            elif dw_type == sdk.NET_SDK_CALLBACK_TYPE_PROGRESS:
                if on_progress:
                    on_progress()
            elif dw_type == sdk.NET_SDK_CALLBACK_TYPE_DATA:
                if on_data:
                    on_data(data)

        _config_callback = build_fremoteconfigcallback(
            _callback,
            sdk.NET_DVR_ACS_EVENT_CFG,
            on_error=lambda e: _event.set(),
        )

        res = run_net_dvr_startremoteconfig(
            self.user_id,
            sdk.NET_DVR_GET_ACS_EVENT,
            _cond,
            _config_callback,
        )

        start = time.monotonic()
        try:
            while True:
                if _event.wait(timeout=0.25):
                    break
                if timeout_s is not None and (time.monotonic() - start) >= float(
                    timeout_s
                ):
                    break
        finally:
            sdk.NET_DVR_StopRemoteConfig(res)

    def get_asc_event(
        self,
        on_data: Callable | None = None,
        on_status: Callable | None = None,
        on_progress: Callable | None = None,
        # Conditions for filtering access control events:
        dw_major: int | None = None,
        dw_minor: int | None = None,
        start_time: datetime.datetime | None = None,
        end_time: datetime.datetime | None = None,
        by_card_no: str | None = None,
        by_name: str | None = None,
        by_pic_enable: Literal[0, 1] | None = None,
        by_time_type: Literal[0, 1] | None = None,
        dw_begin_serial_no: int | None = None,
        dw_end_serial_no: int | None = None,
        dw_iot_channel_no: int | None = None,
        w_inductive_event_type: int | None = None,
        by_search_type: Literal[0, 1, 2] | None = None,
        by_event_attribute: Literal[0, 1, 2] | None = None,
        sz_monitor_id: str | None = None,
        by_employee_no: str | None = None,
    ) -> None:
        assert any(v is not None for v in (on_data, on_status, on_progress)), (
            "At least one callback (on_data, on_status, on_progress) must be provided."
        )

        _cond = build_net_dvr_acs_event_cond(
            dw_major=dw_major,
            dw_minor=dw_minor,
            start_time=start_time,
            end_time=end_time,
            by_card_no=by_card_no,
            by_name=by_name,
            by_pic_enable=by_pic_enable,
            by_time_type=by_time_type,
            dw_begin_serial_no=dw_begin_serial_no,
            dw_end_serial_no=dw_end_serial_no,
            dw_iot_channel_no=dw_iot_channel_no,
            w_inductive_event_type=w_inductive_event_type,
            by_search_type=by_search_type,
            by_event_attribute=by_event_attribute,
            sz_monitor_id=sz_monitor_id,
            by_employee_no=by_employee_no,
        )

        res = run_net_dvr_startremoteconfig(
            self.user_id,
            sdk.NET_DVR_GET_ACS_EVENT,
            _cond,
        )
        event_cfg = sdk.NET_DVR_ACS_EVENT_CFG()
        event_cfg.dwSize = ctypes.sizeof(event_cfg)

        try:
            while True:
                i_ret = sdk.NET_DVR_GetNextRemoteConfig(
                    res,
                    ctypes.byref(event_cfg),
                    ctypes.sizeof(event_cfg),
                )

                if i_ret == sdk.NET_SDK_GET_NEXT_STATUS_SUCCESS:
                    if on_data:
                        on_data(event_cfg)
                    continue

                if i_ret == sdk.NET_SDK_GET_NETX_STATUS_NEED_WAIT:
                    if on_progress:
                        on_progress()
                    time.sleep(0.01)
                    continue

                elif i_ret == sdk.NET_SDK_GET_NEXT_STATUS_FINISH:
                    if on_status:
                        on_status(i_ret, None)
                    break

                elif i_ret == sdk.NET_SDK_GET_NEXT_STATUS_FAILED:
                    code, msg = get_last_error()
                    if on_status:
                        on_status(i_ret, code)
                    raise RuntimeError(
                        f"NET_DVR_GetNextRemoteConfig returned FAILED: {code} {msg}"
                    )

                elif i_ret == -1:
                    code, msg = get_last_error()
                    raise RuntimeError(
                        f"NET_DVR_GetNextRemoteConfig failed: {code} {msg}"
                    )

                else:
                    raise RuntimeError(
                        f"NET_DVR_GetNextRemoteConfig returned unknown status: {i_ret}"
                    )
        finally:
            sdk.NET_DVR_StopRemoteConfig(res)
