from ctypes import Structure, c_char, c_float

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_THERMOMETRY_ALARMRULE_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_THERMOMETRY_ALARMRULE_PARAM, [
    ('byEnable', BYTE),
    ('byRuleID', BYTE),
    ('byRule', BYTE),
    ('byRes', BYTE),
    ('szRuleName', c_char * 32),
    ('fAlert', c_float),
    ('fAlarm', c_float),
    ('fThreshold', c_float),
    ('dwAlertFilteringTime', DWORD),
    ('dwAlarmFilteringTime', DWORD),
    ('byRes1', BYTE * 56),
])

NET_DVR_THERMOMETRY_ALARMRULE_PARAM = struct_tagNET_DVR_THERMOMETRY_ALARMRULE_PARAM
LPNET_DVR_THERMOMETRY_ALARMRULE_PARAM = POINTER(struct_tagNET_DVR_THERMOMETRY_ALARMRULE_PARAM)
tagNET_DVR_THERMOMETRY_ALARMRULE_PARAM = struct_tagNET_DVR_THERMOMETRY_ALARMRULE_PARAM
