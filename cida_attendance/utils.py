import ctypes
import datetime
import platform
import time
from pathlib import Path
from typing import Callable

from cida_attendance.constants import (
    MAX_LEN_XML,
    NET_DVR_GET_ACS_EVENT,
    NET_SDK_CALLBACK_TYPE_DATA,
    NET_SDK_CALLBACK_TYPE_PROGRESS,
    NET_SDK_CALLBACK_TYPE_STATUS,
)
from cida_attendance.structures import (
    NET_DVR_ACS_EVENT_CFG,
    NET_DVR_ACS_EVENT_COND,
    NET_DVR_XML_CONFIG_INPUT,
    NET_DVR_XML_CONFIG_OUTPUT,
)


def get_dll():
    path = Path(__file__).parent.parent / "libs"

    if platform.system() == "Windows":
        path = path / "HCNetSDK.dll"
    elif platform.system() == "Linux":
        path = path / "libhcnetsdk.so"
    else:
        raise RuntimeError("Unsupported platform")
    return ctypes.CDLL(str(path))


dll = get_dll()


class SDKError(Exception):
    pass


def get_last_error():
    dll.NET_DVR_GetLastError.restype = ctypes.c_uint
    error = dll.NET_DVR_GetLastError()
    dll.NET_DVR_GetErrorMsg.restype = ctypes.c_char_p
    error_no = ctypes.c_int(error)
    error_msg = dll.NET_DVR_GetErrorMsg(ctypes.byref(error_no))
    return error, error_msg.decode("ascii")


def net_dvr_xml_config(
    user_id: int,
    url: str,
    in_buffer: str | None = None,
    recv_timeout: int | None = None,
) -> bytes:
    xml_config_input = NET_DVR_XML_CONFIG_INPUT()

    isize = ctypes.sizeof(xml_config_input)
    xml_config_input.dwSize = isize

    irequest = ctypes.create_string_buffer(url.encode("ascii"))
    xml_config_input.lpRequestUrl = ctypes.addressof(irequest)
    xml_config_input.dwRequestUrlLen = len(url)

    if in_buffer is not None:
        ibuffer = ctypes.create_string_buffer(in_buffer.encode("ascii"))
        # xml_config_input.lpInBuffer = ctypes.addressof(ibuffer)
        xml_config_input.lpInBuffer = ctypes.cast(ibuffer, ctypes.c_void_p)
        xml_config_input.dwInBufferSize = len(in_buffer)

    if recv_timeout is not None:
        xml_config_input.dwRecvTimeOut = recv_timeout

    lpInputParam = ctypes.create_string_buffer(isize)
    ctypes.memmove(lpInputParam, ctypes.byref(xml_config_input), isize)

    xml_config_output = NET_DVR_XML_CONFIG_OUTPUT()

    osize = ctypes.sizeof(xml_config_output)
    xml_config_output.dwSize = osize

    ibuffer = ctypes.create_string_buffer(MAX_LEN_XML)
    xml_config_output.lpOutBuffer = ctypes.addressof(ibuffer)
    xml_config_output.dwOutBufferSize = MAX_LEN_XML

    lpOutputParam = ctypes.create_string_buffer(osize)
    ctypes.memmove(lpOutputParam, ctypes.byref(xml_config_output), osize)

    if not dll.NET_DVR_STDXMLConfig(user_id, lpInputParam, lpOutputParam):
        raise SDKError(*get_last_error())

    return ibuffer.value


def structure_to_dict(structure, simple=False):
    data = {}
    for name, type_ in structure._fields_:
        if name.startswith("byRes"):
            continue
        value = getattr(structure, name)
        if not simple:
            if hasattr(value, "to_python"):
                value = value.to_python()
            elif isinstance(value, ctypes.Array):
                try:
                    value = bytes(value).decode("ascii").rstrip("\x00")
                except UnicodeDecodeError:
                    value = "ERROR"
            elif isinstance(value, ctypes.Structure):
                value = structure_to_dict(value)
        data[name] = value
    return data


RemoteConfigCallback = ctypes.CFUNCTYPE(
    None,
    ctypes.c_ulong,
    ctypes.c_void_p,
    ctypes.c_ulong,
    ctypes.c_void_p,
)


def NET_DVR_RemoteConfig(
    user_id: int,
    command: int,
    cond: ctypes.Structure,
    on_status: Callable = None,
    on_progress: Callable = None,
    on_data: Callable = None,
    data_cls: ctypes.Structure = None,
    wait=0.5,
):
    Flag = type("Flag", (object,), {"flag": False})
    flag = Flag()

    @RemoteConfigCallback
    def remote_config_callback(dwType, lpBuffer, dwBufLen, pUserData):
        if dwType == NET_SDK_CALLBACK_TYPE_STATUS:
            buffer = ctypes.cast(lpBuffer, ctypes.c_char_p).value
            flag.flag = True

            if dwBufLen == 4:
                status = int.from_bytes(buffer, "little")
                if on_status:
                    on_status(status, None)
                return

            if dwBufLen == 8:
                status = int.from_bytes(buffer[:4], "little")
                error = int.from_bytes(buffer[4:], "little")
                if on_status:
                    on_status(status, error)
                return

            return

        if dwType == NET_SDK_CALLBACK_TYPE_PROGRESS:
            if on_progress:
                on_progress()
            return

        if dwType == NET_SDK_CALLBACK_TYPE_DATA:
            if on_data:
                if data_cls:
                    detail = ctypes.cast(lpBuffer, ctypes.POINTER(data_cls))
                    on_data(detail.contents)
                else:
                    on_data((lpBuffer, dwBufLen))

    res = dll.NET_DVR_StartRemoteConfig(
        user_id,
        command,
        ctypes.byref(cond),
        ctypes.sizeof(cond),
        remote_config_callback,
        None,
    )

    if res < 0:
        raise SDKError(*get_last_error())

    while not flag.flag:
        time.sleep(wait)

    dll.NET_DVR_StopRemoteConfig(res)


def search_events(
    user_id: int,
    start_date: datetime.datetime,
    end_date: datetime.datetime,
):
    cond = NET_DVR_ACS_EVENT_COND()

    cond.dwMajor = 0x5
    cond.dwMinor = 0x26

    cond.struStartTime.dwYear = start_date.year
    cond.struStartTime.dwMonth = start_date.month
    cond.struStartTime.dwDay = start_date.day
    cond.struStartTime.dwHour = start_date.hour
    cond.struStartTime.dwMinute = start_date.minute
    cond.struStartTime.dwSecond = start_date.second

    cond.struEndTime.dwYear = end_date.year
    cond.struEndTime.dwMonth = end_date.month
    cond.struEndTime.dwDay = end_date.day
    cond.struEndTime.dwHour = end_date.hour
    cond.struEndTime.dwMinute = end_date.minute
    cond.struEndTime.dwSecond = end_date.second

    events = []

    NET_DVR_RemoteConfig(
        user_id,
        NET_DVR_GET_ACS_EVENT,
        cond,
        on_data=events.append,
        data_cls=NET_DVR_ACS_EVENT_CFG,
    )

    return events
