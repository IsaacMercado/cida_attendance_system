from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME


class struct_tagNET_DVR_STATISTIC_DATA_CFG(Structure):
    pass

_S(struct_tagNET_DVR_STATISTIC_DATA_CFG, [
    ('dwSize', DWORD),
    ('dwTypeTarget', DWORD),
    ('struStartTime', NET_DVR_TIME),
    ('struStopTime', NET_DVR_TIME),
    ('byRes', BYTE * 300),
])

NET_DVR_STATISTIC_DATA_CFG = struct_tagNET_DVR_STATISTIC_DATA_CFG
LPNET_DVR_STATISTIC_DATA_CFG = POINTER(struct_tagNET_DVR_STATISTIC_DATA_CFG)
tagNET_DVR_STATISTIC_DATA_CFG = struct_tagNET_DVR_STATISTIC_DATA_CFG
