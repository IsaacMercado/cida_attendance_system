from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_NET_DVR_MONITOR_INFO_RESPONSE(Structure):
    pass

_S(struct_NET_DVR_MONITOR_INFO_RESPONSE, [
    ('dwErrorCode', DWORD),
    ('dwMonId', DWORD),
    ('byRes', BYTE * 4),
])

NET_DVR_MONITOR_INFO_RESPONSE = struct_NET_DVR_MONITOR_INFO_RESPONSE
LPNET_DVR_MONITOR_INFO_RESPONSE = POINTER(struct_NET_DVR_MONITOR_INFO_RESPONSE)
NET_DVR_MONITOR_INFO_RESPONSE = struct_NET_DVR_MONITOR_INFO_RESPONSE
