from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_switch_day_time import NET_DVR_SWITCH_DAY_TIME
from .net_dvr_switch_time_point import NET_DVR_SWITCH_TIME_POINT


class struct_tagNET_DVR_TIME_SWITCH_CFG(Structure):
    pass

_S(struct_tagNET_DVR_TIME_SWITCH_CFG, [
    ('dwSize', DWORD),
    ('struSwitchDayTime', (NET_DVR_SWITCH_DAY_TIME * 8) * 7),
    ('struSwitchTimePoint', NET_DVR_SWITCH_TIME_POINT * 16),
    ('byRes1', BYTE * 3),
    ('byEnable', BYTE),
    ('byRes', BYTE * 60),
])

NET_DVR_TIME_SWITCH_CFG = struct_tagNET_DVR_TIME_SWITCH_CFG
LPNET_DVR_TIME_SWITCH_CFG = POINTER(struct_tagNET_DVR_TIME_SWITCH_CFG)
tagNET_DVR_TIME_SWITCH_CFG = struct_tagNET_DVR_TIME_SWITCH_CFG
