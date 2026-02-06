"""Compat shim (SDK Hikvision).

Históricamente este proyecto tenía un "loader" propio y bindings parciales.
Ahora se usa el wrapper completo generado por ctypesgen en `cida_attendance.sdk`,
que ya incluye su loader multiplataforma.

Este módulo queda como capa de compatibilidad con helpers básicos.
"""

from __future__ import annotations

import ctypes
import datetime
import platform
import sys
import threading
import time
from typing import Callable

from cida_attendance import sdk

MAX_LEN_XML = 10 * 1024 * 1024
XML_ABILITY_IN_LEN = 1024
XML_ABILITY_OUT_LEN = 3 * 1024 * 1024


class SDKError(Exception):
    pass


def get_sdk_version():
    try:
        version = sdk.NET_DVR_GetSDKVersion()
        build = sdk.NET_DVR_GetSDKBuildVersion()
        return {
            "version": version,
            "build": build,
            "version_string": f"{version >> 24}.{(version >> 16) & 0xFF}.{(version >> 8) & 0xFF}.{version & 0xFF}",
            "build_string": f"{build}",
        }
    except Exception as e:
        return {"error": str(e)}


def get_platform_info() -> dict:
    return {
        "platform": platform.system(),
        "sys_platform": sys.platform,
        "python": sys.version,
    }


def init_dll():
    sdk.NET_DVR_Init()
    sdk.NET_DVR_SetConnectTime(2000, 1)
    sdk.NET_DVR_SetReconnect(10000, True)


def cleanup_dll():
    sdk.NET_DVR_Cleanup()


def get_last_error(show_msg: bool = True) -> tuple[int, str | None]:
    error = sdk.NET_DVR_GetLastError()
    if not show_msg:
        return error, None

    error_no = ctypes.c_int(error)
    error_msg = sdk.NET_DVR_GetErrorMsg(ctypes.byref(error_no))
    if not error_msg:
        return error, None
    return error, bytes(error_msg).decode("ascii", errors="ignore")


def build_net_dvr_xml_config_input(
    user_id: int,
    url: str,
    in_buffer: str | None = None,
    recv_timeout: int | None = None,
) -> bytes:
    xml_config_input = sdk.NET_DVR_XML_CONFIG_INPUT()
    xml_config_input.dwSize = ctypes.sizeof(xml_config_input)

    request_buf = ctypes.create_string_buffer(url.encode("ascii"))
    xml_config_input.lpRequestUrl = ctypes.cast(request_buf, ctypes.c_void_p)
    xml_config_input.dwRequestUrlLen = len(url)

    in_buf = None
    if in_buffer is not None:
        in_buf = ctypes.create_string_buffer(in_buffer.encode("ascii"))
        xml_config_input.lpInBuffer = ctypes.cast(in_buf, ctypes.c_void_p)
        xml_config_input.dwInBufferSize = len(in_buffer)

    if recv_timeout is not None:
        xml_config_input.dwRecvTimeOut = int(recv_timeout)

    xml_config_output = sdk.NET_DVR_XML_CONFIG_OUTPUT()
    xml_config_output.dwSize = ctypes.sizeof(xml_config_output)

    out_buf = ctypes.create_string_buffer(MAX_LEN_XML)
    xml_config_output.lpOutBuffer = ctypes.cast(out_buf, ctypes.c_void_p)
    xml_config_output.dwOutBufferSize = MAX_LEN_XML

    status_buf = ctypes.create_string_buffer(1024)
    xml_config_output.lpStatusBuffer = ctypes.cast(status_buf, ctypes.c_void_p)
    xml_config_output.dwStatusSize = ctypes.sizeof(status_buf)

    if not sdk.NET_DVR_STDXMLConfig(
        user_id,
        ctypes.byref(xml_config_input),
        ctypes.byref(xml_config_output),
    ):
        raise SDKError(*get_last_error())

    return out_buf.value


def build_net_dvr_remoteconfig(
    user_id: int,
    command: int,
    cond: ctypes.Structure,
    on_status: Callable = None,
    on_progress: Callable = None,
    on_data: Callable = None,
    data_cls: ctypes.Structure = None,
    timeout_s: float | None = None,
):
    _event = threading.Event()
    callback_error: list[BaseException] = []

    @sdk.fRemoteConfigCallback
    def remote_config_callback(dwType, lpBuffer, dwBufLen, pUserData):
        try:
            if dwType == sdk.NET_SDK_CALLBACK_TYPE_STATUS:
                buffer = ctypes.string_at(lpBuffer, dwBufLen)

                if dwBufLen == 4:
                    status = int.from_bytes(buffer[:4], "little", signed=False)
                    if on_status:
                        on_status(status, None)
                elif dwBufLen == 8:
                    status = int.from_bytes(buffer[:4], "little", signed=False)
                    error = int.from_bytes(buffer[4:8], "little", signed=False)
                    if on_status:
                        on_status(status, error)

                _event.set()
                return

            if dwType == sdk.NET_SDK_CALLBACK_TYPE_PROGRESS:
                if on_progress:
                    on_progress()
                return

            if dwType == sdk.NET_SDK_CALLBACK_TYPE_DATA:
                if on_data:
                    if data_cls:
                        detail = ctypes.cast(lpBuffer, ctypes.POINTER(data_cls))
                        on_data(detail.contents)
                    else:
                        on_data((lpBuffer, dwBufLen))
        except BaseException as e:
            callback_error.append(e)
            _event.set()
            return

    res = sdk.NET_DVR_StartRemoteConfig(
        user_id,
        command,
        ctypes.byref(cond),
        ctypes.sizeof(cond),
        remote_config_callback,
        None,
    )

    if res < 0:
        raise SDKError(*get_last_error())

    start = time.monotonic()
    try:
        while True:
            if _event.wait(timeout=0.25):
                break
            if timeout_s is not None and (time.monotonic() - start) >= float(timeout_s):
                break
    finally:
        sdk.NET_DVR_StopRemoteConfig(res)

    if callback_error:
        raise callback_error[0]

    return


def build_net_dvr_user_login_info(device_address, username, password, port=8000):
    login_info = sdk.NET_DVR_USER_LOGIN_INFO()
    # En el wrapper generado, estos campos son `c_char_Array_*`.
    # Asignar `bytes` es lo correcto; asignar arrays de `c_byte` provoca TypeError.
    login_info.sDeviceAddress = device_address.ljust(
        sdk.NET_DVR_DEV_ADDRESS_MAX_LEN, b"\x00"
    )
    login_info.wPort = int(port)
    login_info.bUseAsynLogin = 0
    login_info.sUserName = username.ljust(sdk.NET_DVR_LOGIN_USERNAME_MAX_LEN, b"\x00")
    login_info.sPassword = password.ljust(sdk.NET_DVR_LOGIN_PASSWD_MAX_LEN, b"\x00")
    return login_info


def build_datetime_to_net_dvr_time(dt: datetime.datetime, structure=None):
    net_dvr_time = structure or sdk.NET_DVR_TIME()
    net_dvr_time.dwYear = dt.year
    net_dvr_time.dwMonth = dt.month
    net_dvr_time.dwDay = dt.day
    net_dvr_time.dwHour = dt.hour
    net_dvr_time.dwMinute = dt.minute
    net_dvr_time.dwSecond = dt.second
    return net_dvr_time


def build_datetime_from_net_dvr_time(
    net_dvr_time,
    tz: datetime.timezone = None,
) -> datetime.datetime:
    return datetime.datetime(
        net_dvr_time.dwYear,
        net_dvr_time.dwMonth,
        net_dvr_time.dwDay,
        net_dvr_time.dwHour,
        net_dvr_time.dwMinute,
        net_dvr_time.dwSecond,
        tzinfo=tz,
    )


def build_net_dvr_acs_event_cond(
    major: int = None,
    minor: int = None,
    start_time: datetime.datetime = None,
    end_time: datetime.datetime = None,
):
    cond = sdk.NET_DVR_ACS_EVENT_COND()
    cond.dwSize = ctypes.sizeof(cond)

    if major is not None:
        cond.dwMajor = major

    if minor is not None:
        cond.dwMinor = minor

    if start_time is not None:
        build_datetime_to_net_dvr_time(start_time, cond.struStartTime)

    if end_time is not None:
        build_datetime_to_net_dvr_time(end_time, cond.struEndTime)

    return cond
