from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_time_v30 import NET_DVR_TIME_V30


class struct_tagNET_DVR_UPLOAD_VIDEO_INFO(Structure):
    pass

_S(struct_tagNET_DVR_UPLOAD_VIDEO_INFO, [
    ('dwSize', DWORD),
    ('dwVideoMangeNo', DWORD),
    ('byVideoType', BYTE),
    ('byRes1', BYTE * 3),
    ('sVideoName', BYTE * 32),
    ('struTime', NET_DVR_TIME_V30),
    ('byRes', BYTE * 132),
])

NET_DVR_UPLOAD_VIDEO_INFO = struct_tagNET_DVR_UPLOAD_VIDEO_INFO
LPNET_DVR_UPLOAD_VIDEO_INFO = POINTER(struct_tagNET_DVR_UPLOAD_VIDEO_INFO)
tagNET_DVR_UPLOAD_VIDEO_INFO = struct_tagNET_DVR_UPLOAD_VIDEO_INFO
