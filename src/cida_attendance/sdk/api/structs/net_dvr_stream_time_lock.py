from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME
from .net_dvr_stream_info import NET_DVR_STREAM_INFO
from .net_dvr_time_ex import NET_DVR_TIME_EX


class struct_tagNET_DVR_STREAM_TIME_LOCK(Structure):
    pass

_S(struct_tagNET_DVR_STREAM_TIME_LOCK, [
    ('dwSize', DWORD),
    ('strBeginTime', NET_DVR_TIME),
    ('strEndTime', NET_DVR_TIME),
    ('struStreamInfo', NET_DVR_STREAM_INFO),
    ('dwRecordType', DWORD),
    ('dwLockDuration', DWORD),
    ('strUnlockTimePoint', NET_DVR_TIME_EX),
    ('byISO8601', BYTE),
    ('cTimeDifferenceH', c_char),
    ('cTimeDifferenceM', c_char),
    ('byRes', BYTE * 1),
])

NET_DVR_STREAM_TIME_LOCK = struct_tagNET_DVR_STREAM_TIME_LOCK
LPNET_DVR_STREAM_TIME_LOCK = POINTER(struct_tagNET_DVR_STREAM_TIME_LOCK)
tagNET_DVR_STREAM_TIME_LOCK = struct_tagNET_DVR_STREAM_TIME_LOCK
