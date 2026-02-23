from ctypes import Structure, c_float

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER, String
from .net_ptz_info import NET_PTZ_INFO
from .net_vca_point import NET_VCA_POINT
from .net_vca_polygon import NET_VCA_POLYGON


class struct_tagNET_DVR_THERMOMETRY_ALARM(Structure):
    pass

_S(struct_tagNET_DVR_THERMOMETRY_ALARM, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('byRuleID', BYTE),
    ('byThermometryUnit', BYTE),
    ('wPresetNo', WORD),
    ('struPtzInfo', NET_PTZ_INFO),
    ('byAlarmLevel', BYTE),
    ('byAlarmType', BYTE),
    ('byAlarmRule', BYTE),
    ('byRuleCalibType', BYTE),
    ('struPoint', NET_VCA_POINT),
    ('struRegion', NET_VCA_POLYGON),
    ('fRuleTemperature', c_float),
    ('fCurrTemperature', c_float),
    ('dwPicLen', DWORD),
    ('dwThermalPicLen', DWORD),
    ('dwThermalInfoLen', DWORD),
    ('pPicBuff', String),
    ('pThermalPicBuff', String),
    ('pThermalInfoBuff', String),
    ('struHighestPoint', NET_VCA_POINT),
    ('fToleranceTemperature', c_float),
    ('dwAlertFilteringTime', DWORD),
    ('dwAlarmFilteringTime', DWORD),
    ('dwTemperatureSuddenChangeCycle', DWORD),
    ('fTemperatureSuddenChangeValue', c_float),
    ('byPicTransType', BYTE),
    ('byRes1', BYTE * 3),
    ('dwVisibleChannel', DWORD),
    ('dwRelativeTime', DWORD),
    ('dwAbsTime', DWORD),
    ('fAlarmRuleTemperature', c_float),
    ('byRes', BYTE * 20),
])

NET_DVR_THERMOMETRY_ALARM = struct_tagNET_DVR_THERMOMETRY_ALARM
LPNET_DVR_THERMOMETRY_ALARM = POINTER(struct_tagNET_DVR_THERMOMETRY_ALARM)
tagNET_DVR_THERMOMETRY_ALARM = struct_tagNET_DVR_THERMOMETRY_ALARM
