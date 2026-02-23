from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_NOTICE_VIDEO_DATA(Structure):
    pass

_S(struct_tagNET_DVR_NOTICE_VIDEO_DATA, [
    ('dwSize', DWORD),
    ('dwFileSize', DWORD),
    ('byNoticeNumber', BYTE * 32),
    ('byRes', BYTE * 2016),
])

NET_DVR_NOTICE_VIDEO_DATA = struct_tagNET_DVR_NOTICE_VIDEO_DATA
LPNET_DVR_NOTICE_VIDEO_DATA = POINTER(struct_tagNET_DVR_NOTICE_VIDEO_DATA)
tagNET_DVR_NOTICE_VIDEO_DATA = struct_tagNET_DVR_NOTICE_VIDEO_DATA
