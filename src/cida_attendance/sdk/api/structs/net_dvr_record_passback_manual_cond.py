from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_stream_info import NET_DVR_STREAM_INFO
from .net_dvr_time_ex import NET_DVR_TIME_EX


class struct_tagNET_DVR_RECORD_PASSBACK_MANUAL_COND(Structure):
    pass

_S(struct_tagNET_DVR_RECORD_PASSBACK_MANUAL_COND, [
    ('dwSize', DWORD),
    ('byType', BYTE),
    ('byTimeSegmentQuety', BYTE),
    ('byRes1', BYTE * 2),
    ('struStreamInfo', NET_DVR_STREAM_INFO),
    ('struBeginTime', NET_DVR_TIME_EX),
    ('struEndTime', NET_DVR_TIME_EX),
    ('dwTaskID', DWORD),
    ('byRes', BYTE * 108),
])

NET_DVR_RECORD_PASSBACK_MANUAL_COND = struct_tagNET_DVR_RECORD_PASSBACK_MANUAL_COND
LPNET_DVR_RECORD_PASSBACK_MANUAL_COND = POINTER(struct_tagNET_DVR_RECORD_PASSBACK_MANUAL_COND)
tagNET_DVR_RECORD_PASSBACK_MANUAL_COND = struct_tagNET_DVR_RECORD_PASSBACK_MANUAL_COND
