from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_stream_info import NET_DVR_STREAM_INFO
from .net_dvr_time_ex import NET_DVR_TIME_EX


class struct_tagNET_DVR_RECORD_SEGMENT_COND_(Structure):
    pass

_S(struct_tagNET_DVR_RECORD_SEGMENT_COND_, [
    ('dwSize', DWORD),
    ('struStreanInfo', NET_DVR_STREAM_INFO),
    ('struStartTime', NET_DVR_TIME_EX),
    ('struStopTime', NET_DVR_TIME_EX),
    ('byRes', BYTE * 256),
])

NET_DVR_RECORD_SEGMENT_COND = struct_tagNET_DVR_RECORD_SEGMENT_COND_
LPNET_DVR_RECORD_SEGMENT_COND = POINTER(struct_tagNET_DVR_RECORD_SEGMENT_COND_)
tagNET_DVR_RECORD_SEGMENT_COND_ = struct_tagNET_DVR_RECORD_SEGMENT_COND_
