from ctypes import Structure, c_int

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SENSOR_ADJUSTMENT_INFO(Structure):
    pass

_S(struct_tagNET_DVR_SENSOR_ADJUSTMENT_INFO, [
    ('dwSize', DWORD),
    ('iPan', c_int),
    ('iTilt', c_int),
    ('iRotation', c_int),
    ('iFieldAngle', c_int),
    ('byR', BYTE),
    ('byG', BYTE),
    ('byB', BYTE),
    ('byRgbType', BYTE),
    ('byBrightness', BYTE),
    ('byRes', BYTE * 3),
    ('wRex', WORD),
    ('wGex', WORD),
    ('wBex', WORD),
    ('byRes1', BYTE * 114),
])

NET_DVR_SENSOR_ADJUSTMENT_INFO = struct_tagNET_DVR_SENSOR_ADJUSTMENT_INFO
LPNET_DVR_SENSOR_ADJUSTMENT_INFO = POINTER(struct_tagNET_DVR_SENSOR_ADJUSTMENT_INFO)
tagNET_DVR_SENSOR_ADJUSTMENT_INFO = struct_tagNET_DVR_SENSOR_ADJUSTMENT_INFO
