from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER, String


class struct_tagNET_DVR_NOTICE_VIDEO_DATA_CFG(Structure):
    pass

_S(struct_tagNET_DVR_NOTICE_VIDEO_DATA_CFG, [
    ('dwSize', DWORD),
    ('dwDataLen', DWORD),
    ('pDataBuffer', String),
    ('byDataType', BYTE),
    ('byRes', BYTE * 63),
])

NET_DVR_NOTICE_VIDEO_DATA_CFG = struct_tagNET_DVR_NOTICE_VIDEO_DATA_CFG
LPNET_DVR_NOTICE_VIDEO_DATA_CFG = POINTER(struct_tagNET_DVR_NOTICE_VIDEO_DATA_CFG)
tagNET_DVR_NOTICE_VIDEO_DATA_CFG = struct_tagNET_DVR_NOTICE_VIDEO_DATA_CFG
