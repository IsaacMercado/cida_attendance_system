from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME
from .net_dvr_time_ex import NET_DVR_TIME_EX


class struct_tagNET_DVR_TIME_LOCK(Structure):
    pass

_S(struct_tagNET_DVR_TIME_LOCK, [
    ('dwSize', DWORD),
    ('strBeginTime', NET_DVR_TIME),
    ('strEndTime', NET_DVR_TIME),
    ('dwChannel', DWORD),
    ('dwRecordType', DWORD),
    ('dwLockDuration', DWORD),
    ('strUnlockTimePoint', NET_DVR_TIME_EX),
    ('byRes', BYTE * 4),
])

NET_DVR_TIME_LOCK = struct_tagNET_DVR_TIME_LOCK
LPNET_DVR_TIME_LOCK = POINTER(struct_tagNET_DVR_TIME_LOCK)
tagNET_DVR_TIME_LOCK = struct_tagNET_DVR_TIME_LOCK
