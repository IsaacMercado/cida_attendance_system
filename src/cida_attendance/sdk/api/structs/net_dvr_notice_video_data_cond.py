from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_NOTICE_VIDEO_DATA_COND(Structure):
    pass

_S(struct_tagNET_DVR_NOTICE_VIDEO_DATA_COND, [
    ('dwSize', DWORD),
    ('byRes', BYTE * 256),
])

NET_DVR_NOTICE_VIDEO_DATA_COND = struct_tagNET_DVR_NOTICE_VIDEO_DATA_COND
LPNET_DVR_NOTICE_VIDEO_DATA_COND = POINTER(struct_tagNET_DVR_NOTICE_VIDEO_DATA_COND)
tagNET_DVR_NOTICE_VIDEO_DATA_COND = struct_tagNET_DVR_NOTICE_VIDEO_DATA_COND
