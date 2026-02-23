from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, INT64
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_VIDEO_IMG_DB_CFG(Structure):
    pass

_S(struct_tagNET_DVR_VIDEO_IMG_DB_CFG, [
    ('dwSize', DWORD),
    ('i64Capacity', INT64),
    ('i64UsedSpace', INT64),
    ('i64AvailableSpace', INT64),
    ('byRes', BYTE * 256),
])

NET_DVR_VIDEO_IMG_DB_CFG = struct_tagNET_DVR_VIDEO_IMG_DB_CFG
LPNET_DVR_VIDEO_IMG_DB_CFG = POINTER(struct_tagNET_DVR_VIDEO_IMG_DB_CFG)
tagNET_DVR_VIDEO_IMG_DB_CFG = struct_tagNET_DVR_VIDEO_IMG_DB_CFG
