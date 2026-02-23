from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PLATFORM_VERIFY_CFG(Structure):
    pass

_S(struct_tagNET_DVR_PLATFORM_VERIFY_CFG, [
    ('dwSize', DWORD),
    ('dwDoorNo', DWORD),
    ('byResultType', BYTE),
    ('byRes1', BYTE * 3),
    ('byScreenDisplay', BYTE * 512),
    ('byRes', BYTE * 300),
])

NET_DVR_PLATFORM_VERIFY_CFG = struct_tagNET_DVR_PLATFORM_VERIFY_CFG
LPNET_DVR_PLATFORM_VERIFY_CFG = POINTER(struct_tagNET_DVR_PLATFORM_VERIFY_CFG)
tagNET_DVR_PLATFORM_VERIFY_CFG = struct_tagNET_DVR_PLATFORM_VERIFY_CFG
