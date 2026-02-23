from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_stream_info import NET_DVR_STREAM_INFO
from .net_dvr_time_ex import NET_DVR_TIME_EX


class struct_tagNET_DVR_RECORD_CHECK_COND(Structure):
    pass

_S(struct_tagNET_DVR_RECORD_CHECK_COND, [
    ('dwSize', DWORD),
    ('struStreamInfo', NET_DVR_STREAM_INFO),
    ('byCheckType', BYTE),
    ('byRes1', BYTE * 3),
    ('struBeginTime', NET_DVR_TIME_EX),
    ('struEndTime', NET_DVR_TIME_EX),
    ('byRes', BYTE * 128),
])

NET_DVR_RECORD_CHECK_COND = struct_tagNET_DVR_RECORD_CHECK_COND
LPNET_DVR_RECORD_CHECK_COND = POINTER(struct_tagNET_DVR_RECORD_CHECK_COND)
tagNET_DVR_RECORD_CHECK_COND = struct_tagNET_DVR_RECORD_CHECK_COND
