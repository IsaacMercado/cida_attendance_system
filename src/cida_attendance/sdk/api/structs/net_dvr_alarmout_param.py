from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ALARMOUT_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_ALARMOUT_PARAM, [
    ('dwSize', DWORD),
    ('byName', BYTE * 32),
    ('wDelay', WORD),
    ('wTriggerIndex', WORD),
    ('byAssociateAlarmIn', BYTE * 512),
    ('byModuleType', BYTE),
    ('byModuleStatus', BYTE),
    ('wModuleAddress', WORD),
    ('byModuleChan', BYTE),
    ('byWorkMode', BYTE),
    ('byAlarmOutMode', BYTE),
    ('byTimeOn', BYTE),
    ('byTimeOff', BYTE),
    ('byDurationConstOutputEnable', BYTE),
    ('byRes2', BYTE * 50),
])

NET_DVR_ALARMOUT_PARAM = struct_tagNET_DVR_ALARMOUT_PARAM
LPNET_DVR_ALARMOUT_PARAM = POINTER(struct_tagNET_DVR_ALARMOUT_PARAM)
tagNET_DVR_ALARMOUT_PARAM = struct_tagNET_DVR_ALARMOUT_PARAM
