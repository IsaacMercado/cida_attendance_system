from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_LOCKED_INFO(Structure):
    pass

_S(struct_tagNET_DVR_LOCKED_INFO, [
    ('dwSize', DWORD),
    ('byIPType', BYTE),
    ('byRes1', BYTE * 3),
    ('struIPAddress', NET_DVR_IPADDR),
    ('byRes', BYTE * 20),
])

NET_DVR_LOCKED_INFO = struct_tagNET_DVR_LOCKED_INFO
LPNET_DVR_LOCKED_INFO = POINTER(struct_tagNET_DVR_LOCKED_INFO)
tagNET_DVR_LOCKED_INFO = struct_tagNET_DVR_LOCKED_INFO
