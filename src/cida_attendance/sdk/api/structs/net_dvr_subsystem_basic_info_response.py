from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_NET_DVR_SUBSYSTEM_BASIC_INFO_RESPONSE(Structure):
    pass

_S(struct_NET_DVR_SUBSYSTEM_BASIC_INFO_RESPONSE, [
    ('dwSize', DWORD),
    ('dwErrorCode', DWORD),
    ('byDevNo', BYTE),
    ('bySubSystemNo', BYTE),
    ('byRes', BYTE * 30),
])

NET_DVR_SUBSYSTEM_BASIC_INFO_RESPONSE = struct_NET_DVR_SUBSYSTEM_BASIC_INFO_RESPONSE
LPNET_DVR_SUBSYSTEM_BASIC_INFO_RESPONSE = POINTER(struct_NET_DVR_SUBSYSTEM_BASIC_INFO_RESPONSE)
NET_DVR_SUBSYSTEM_BASIC_INFO_RESPONSE = struct_NET_DVR_SUBSYSTEM_BASIC_INFO_RESPONSE
