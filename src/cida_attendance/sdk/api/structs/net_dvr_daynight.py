from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_DAYNIGHT(Structure):
    pass

_S(struct_tagNET_DVR_DAYNIGHT, [
    ('byDayNightFilterType', BYTE),
    ('bySwitchScheduleEnabled', BYTE),
    ('byBeginTime', BYTE),
    ('byEndTime', BYTE),
    ('byDayToNightFilterLevel', BYTE),
    ('byNightToDayFilterLevel', BYTE),
    ('byDayNightFilterTime', BYTE),
    ('byBeginTimeMin', BYTE),
    ('byBeginTimeSec', BYTE),
    ('byEndTimeMin', BYTE),
    ('byEndTimeSec', BYTE),
    ('byAlarmTrigState', BYTE),
])

NET_DVR_DAYNIGHT = struct_tagNET_DVR_DAYNIGHT
LPNET_DVR_DAYNIGHT = POINTER(struct_tagNET_DVR_DAYNIGHT)
tagNET_DVR_DAYNIGHT = struct_tagNET_DVR_DAYNIGHT
