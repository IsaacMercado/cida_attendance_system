from ctypes import Structure, c_float

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER, String
from .net_ptz_info import NET_PTZ_INFO
from .net_vca_point import NET_VCA_POINT
from .net_vca_polygon import NET_VCA_POLYGON


class struct_tagNET_DVR_THERMOMETRY_DIFF_ALARM(Structure):
    pass

_S(struct_tagNET_DVR_THERMOMETRY_DIFF_ALARM, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('byAlarmID1', BYTE),
    ('byAlarmID2', BYTE),
    ('wPresetNo', WORD),
    ('byAlarmLevel', BYTE),
    ('byAlarmType', BYTE),
    ('byAlarmRule', BYTE),
    ('byRuleCalibType', BYTE),
    ('struPoint', NET_VCA_POINT * 2),
    ('struRegion', NET_VCA_POLYGON * 2),
    ('fRuleTemperatureDiff', c_float),
    ('fCurTemperatureDiff', c_float),
    ('struPtzInfo', NET_PTZ_INFO),
    ('dwPicLen', DWORD),
    ('dwThermalPicLen', DWORD),
    ('dwThermalInfoLen', DWORD),
    ('pPicBuff', String),
    ('pThermalPicBuff', String),
    ('pThermalInfoBuff', String),
    ('byThermometryUnit', BYTE),
    ('byPicTransType', BYTE),
    ('byRes1', BYTE * 2),
    ('fToleranceTemperature', c_float),
    ('dwAlarmFilteringTime', DWORD),
    ('dwVisibleChannel', DWORD),
    ('byRes', BYTE * 48),
])

NET_DVR_THERMOMETRY_DIFF_ALARM = struct_tagNET_DVR_THERMOMETRY_DIFF_ALARM
LPNET_DVR_THERMOMETRY_DIFF_ALARM = POINTER(struct_tagNET_DVR_THERMOMETRY_DIFF_ALARM)
tagNET_DVR_THERMOMETRY_DIFF_ALARM = struct_tagNET_DVR_THERMOMETRY_DIFF_ALARM
