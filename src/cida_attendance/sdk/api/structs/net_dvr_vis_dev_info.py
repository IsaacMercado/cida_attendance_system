from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_VIS_DEV_INFO(Structure):
    pass

_S(struct_tagNET_DVR_VIS_DEV_INFO, [
    ('dwSize', DWORD),
    ('szDevNumber', BYTE * 32),
    ('byRes', BYTE * 64),
])

NET_DVR_VIS_DEV_INFO = struct_tagNET_DVR_VIS_DEV_INFO
LPNET_DVR_VIS_DEV_INFO = POINTER(struct_tagNET_DVR_VIS_DEV_INFO)
tagNET_DVR_VIS_DEV_INFO = struct_tagNET_DVR_VIS_DEV_INFO
