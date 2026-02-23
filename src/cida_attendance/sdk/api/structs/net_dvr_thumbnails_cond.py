from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_stream_info import NET_DVR_STREAM_INFO
from .net_dvr_time_v30 import NET_DVR_TIME_V30


class struct_tagNET_DVR_THUMBNAILS_COND(Structure):
    pass

_S(struct_tagNET_DVR_THUMBNAILS_COND, [
    ('dwSize', DWORD),
    ('struStreamInfo', NET_DVR_STREAM_INFO),
    ('bySearchDataType', BYTE),
    ('byRes1', BYTE * 3),
    ('struStartTime', NET_DVR_TIME_V30),
    ('struStopTime', NET_DVR_TIME_V30),
    ('dwIntervalTime', DWORD),
    ('byRes2', BYTE * 512),
])

NET_DVR_THUMBNAILS_COND = struct_tagNET_DVR_THUMBNAILS_COND
LPNET_DVR_THUMBNAILS_COND = POINTER(struct_tagNET_DVR_THUMBNAILS_COND)
tagNET_DVR_THUMBNAILS_COND = struct_tagNET_DVR_THUMBNAILS_COND
