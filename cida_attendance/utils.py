import ctypes
import platform
import threading
from pathlib import Path
from typing import Callable

from cida_attendance.constants import (
    MAX_LEN_XML,
    NET_SDK_CALLBACK_TYPE_DATA,
    NET_SDK_CALLBACK_TYPE_PROGRESS,
    NET_SDK_CALLBACK_TYPE_STATUS,
)
from cida_attendance.structures import (
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

    dll = ctypes.CDLL(str(path))

    dll.NET_DVR_GetLastError.restype = ctypes.c_uint
    dll.NET_DVR_GetErrorMsg.restype = ctypes.c_char_p

    return dll


dll = get_dll()


def init_dll():
    dll.NET_DVR_Init()
    dll.NET_DVR_SetConnectTime(2000, 1)
    dll.NET_DVR_SetReconnect(10000, True)


def cleanup_dll():
    dll.NET_DVR_Cleanup()


class SDKError(Exception):
    pass


def get_last_error(show_msg: bool = True) -> tuple[int, str | None]:
    error = dll.NET_DVR_GetLastError()
    if not show_msg:
        return error, None

    error_no = ctypes.c_int(error)
    error_msg = dll.NET_DVR_GetErrorMsg(ctypes.byref(error_no))
    return error, error_msg and error_msg.decode("ascii")


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
):
    _event = threading.Event()

    @RemoteConfigCallback
    def remote_config_callback(dwType, lpBuffer, dwBufLen, pUserData):
        if dwType == NET_SDK_CALLBACK_TYPE_STATUS:
            buffer = ctypes.cast(lpBuffer, ctypes.c_char_p).value

            if dwBufLen == 4:
                status = int.from_bytes(buffer, "little")
                if on_status:
                    on_status(status, None)

            elif dwBufLen == 8:
                status = int.from_bytes(buffer[:4], "little")
                error = int.from_bytes(buffer[4:], "little")
                if on_status:
                    on_status(status, error)

            _event.set()

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

    _event.wait()
    if _event.is_set():
        return

    dll.NET_DVR_StopRemoteConfig(res)
