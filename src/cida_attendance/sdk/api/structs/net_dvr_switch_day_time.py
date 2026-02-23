from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_385 import NET_DVR_DAYTIME


class struct_tagNET_DVR_SWITCH_DAY_TIME(Structure):
    pass

_S(struct_tagNET_DVR_SWITCH_DAY_TIME, [
    ('byEnable', BYTE),
    ('bySwitchType', BYTE),
    ('byRes1', BYTE * 2),
    ('struTimePoint', NET_DVR_DAYTIME),
    ('byRes2', BYTE * 8),
])

NET_DVR_SWITCH_DAY_TIME = struct_tagNET_DVR_SWITCH_DAY_TIME
LPNET_DVR_SWITCH_DAY_TIME = POINTER(struct_tagNET_DVR_SWITCH_DAY_TIME)
tagNET_DVR_SWITCH_DAY_TIME = struct_tagNET_DVR_SWITCH_DAY_TIME
