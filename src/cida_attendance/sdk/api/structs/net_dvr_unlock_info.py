from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_UNLOCK_INFO(Structure):
    pass

_S(struct_tagNET_DVR_UNLOCK_INFO, [
    ('dwSize', DWORD),
    ('byUnlockType', BYTE),
    ('byIPVersion', BYTE),
    ('byRes1', BYTE * 2),
    ('struIPAddr', NET_DVR_IPADDR),
    ('byRes', BYTE * 64),
])

NET_DVR_UNLOCK_INFO = struct_tagNET_DVR_UNLOCK_INFO
LPNET_DVR_UNLOCK_INFO = POINTER(struct_tagNET_DVR_UNLOCK_INFO)
tagNET_DVR_UNLOCK_INFO = struct_tagNET_DVR_UNLOCK_INFO
