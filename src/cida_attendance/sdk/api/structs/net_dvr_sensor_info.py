from ctypes import Structure, c_float

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SENSOR_INFO(Structure):
    pass

_S(struct_tagNET_DVR_SENSOR_INFO, [
    ('dwSize', DWORD),
    ('byName', BYTE * 32),
    ('byEnable', BYTE),
    ('byValid', BYTE),
    ('byType', BYTE),
    ('byAlarmMode', BYTE),
    ('fMeasureHigh', c_float),
    ('fMeasureLow', c_float),
    ('fAlarm1', c_float),
    ('fAlarm2', c_float),
    ('fAlarm3', c_float),
    ('fAlarm4', c_float),
    ('dwOsdCfg', DWORD),
    ('fSensitive', c_float),
    ('bySensorStandard', BYTE),
    ('byChan', BYTE),
    ('byRes3', BYTE * 114),
])

NET_DVR_SENSOR_INFO = struct_tagNET_DVR_SENSOR_INFO
LPNET_DVR_SENSOR_INFO = POINTER(struct_tagNET_DVR_SENSOR_INFO)
tagNET_DVR_SENSOR_INFO = struct_tagNET_DVR_SENSOR_INFO
