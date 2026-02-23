from ctypes import Structure, c_float

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SENSOR_ALARM(Structure):
    pass

_S(struct_tagNET_DVR_SENSOR_ALARM, [
    ('dwSize', DWORD),
    ('dwAbsTime', DWORD),
    ('byName', BYTE * 32),
    ('bySensorChannel', BYTE),
    ('byType', BYTE),
    ('byAlarmType', BYTE),
    ('byAlarmMode', BYTE),
    ('fValue', c_float),
    ('fOriginalValue', c_float),
    ('byRes2', BYTE * 28),
])

NET_DVR_SENSOR_ALARM = struct_tagNET_DVR_SENSOR_ALARM
LPNET_DVR_SENSOR_ALARM = POINTER(struct_tagNET_DVR_SENSOR_ALARM)
tagNET_DVR_SENSOR_ALARM = struct_tagNET_DVR_SENSOR_ALARM
