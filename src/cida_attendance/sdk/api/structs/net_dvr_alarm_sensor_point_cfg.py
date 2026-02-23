from ctypes import Structure, c_char, c_int

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ALARM_SENSOR_POINT_CFG(Structure):
    pass

_S(struct_tagNET_DVR_ALARM_SENSOR_POINT_CFG, [
    ('nMeasureHigh', c_int),
    ('nMeasureLow', c_int),
    ('byAlarmMode', BYTE),
    ('byRes1', BYTE * 3),
    ('nAlarmValue', c_int * 4),
    ('dwOsdCfg', DWORD),
    ('dwSensitive', DWORD),
    ('dwIPChanOsd', DWORD),
    ('szOSDUnit', c_char * 8),
    ('byRes', BYTE * 16),
])

NET_DVR_ALARM_SENSOR_POINT_CFG = struct_tagNET_DVR_ALARM_SENSOR_POINT_CFG
LPNET_DVR_ALARM_SENSOR_POINT_CFG = POINTER(struct_tagNET_DVR_ALARM_SENSOR_POINT_CFG)
tagNET_DVR_ALARM_SENSOR_POINT_CFG = struct_tagNET_DVR_ALARM_SENSOR_POINT_CFG
