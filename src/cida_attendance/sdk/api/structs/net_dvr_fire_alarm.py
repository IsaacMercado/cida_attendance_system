from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_time_v30 import NET_DVR_TIME_V30


class struct_tagNET_DVR_FIRE_ALARM(Structure):
    pass

_S(struct_tagNET_DVR_FIRE_ALARM, [
    ('dwSize', DWORD),
    ('struAlarmTime', NET_DVR_TIME_V30),
    ('byRes', BYTE * 128),
])

NET_DVR_FIRE_ALARM = struct_tagNET_DVR_FIRE_ALARM
LPNET_DVR_FIRE_ALARM = POINTER(struct_tagNET_DVR_FIRE_ALARM)
tagNET_DVR_FIRE_ALARM = struct_tagNET_DVR_FIRE_ALARM
