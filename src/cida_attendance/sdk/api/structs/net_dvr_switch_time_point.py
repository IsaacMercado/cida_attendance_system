from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_system_time import NET_DVR_SYSTEM_TIME


class struct_tagNET_DVR_SWITCH_TIME_POINT(Structure):
    pass

_S(struct_tagNET_DVR_SWITCH_TIME_POINT, [
    ('byEnable', BYTE),
    ('bySwitchType', BYTE),
    ('byRes1', BYTE * 2),
    ('struTimePoint', NET_DVR_SYSTEM_TIME),
    ('byRes2', BYTE * 16),
])

NET_DVR_SWITCH_TIME_POINT = struct_tagNET_DVR_SWITCH_TIME_POINT
LPNET_DVR_SWITCH_TIME_POINT = POINTER(struct_tagNET_DVR_SWITCH_TIME_POINT)
tagNET_DVR_SWITCH_TIME_POINT = struct_tagNET_DVR_SWITCH_TIME_POINT
