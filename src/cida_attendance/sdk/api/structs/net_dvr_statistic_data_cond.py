from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME


class struct_tagNET_DVR_STATISTIC_DATA_COND(Structure):
    pass

_S(struct_tagNET_DVR_STATISTIC_DATA_COND, [
    ('dwSize', DWORD),
    ('dwTypeTarget', DWORD),
    ('struStartTime', NET_DVR_TIME),
    ('struStopTime', NET_DVR_TIME),
    ('byRes', BYTE * 280),
])

NET_DVR_STATISTIC_DATA_COND = struct_tagNET_DVR_STATISTIC_DATA_COND
LPNET_DVR_STATISTIC_DATA_COND = POINTER(struct_tagNET_DVR_STATISTIC_DATA_COND)
tagNET_DVR_STATISTIC_DATA_COND = struct_tagNET_DVR_STATISTIC_DATA_COND
