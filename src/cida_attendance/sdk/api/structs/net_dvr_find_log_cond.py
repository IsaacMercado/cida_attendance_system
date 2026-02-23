from ctypes import Structure, c_int

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_time_v50 import NET_DVR_TIME_V50


class struct_tagNET_DVR_FIND_LOG_COND(Structure):
    pass

_S(struct_tagNET_DVR_FIND_LOG_COND, [
    ('dwSelectMode', DWORD),
    ('dwMainType', DWORD),
    ('dwSubType', DWORD),
    ('struStartTime', NET_DVR_TIME_V50),
    ('struEndTime', NET_DVR_TIME_V50),
    ('bOnlySmart', c_int),
    ('byRes', BYTE * 128),
])

NET_DVR_FIND_LOG_COND = struct_tagNET_DVR_FIND_LOG_COND
LPNET_DVR_FIND_LOG_COND = POINTER(struct_tagNET_DVR_FIND_LOG_COND)
tagNET_DVR_FIND_LOG_COND = struct_tagNET_DVR_FIND_LOG_COND
