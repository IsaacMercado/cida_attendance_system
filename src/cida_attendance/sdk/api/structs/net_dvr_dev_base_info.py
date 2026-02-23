from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_DEV_BASE_INFO(Structure):
    pass

_S(struct_tagNET_DVR_DEV_BASE_INFO, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byDeviceType', BYTE),
    ('byRes1', BYTE * 2),
    ('sDevName', BYTE * 32),
    ('byRes2', BYTE * 24),
])

NET_DVR_DEV_BASE_INFO = struct_tagNET_DVR_DEV_BASE_INFO
LPNET_DVR_DEV_BASE_INFO = POINTER(struct_tagNET_DVR_DEV_BASE_INFO)
tagNET_DVR_DEV_BASE_INFO = struct_tagNET_DVR_DEV_BASE_INFO
