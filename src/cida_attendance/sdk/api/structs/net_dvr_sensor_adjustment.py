from ctypes import Structure, c_int

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SENSOR_ADJUSTMENT(Structure):
    pass

_S(struct_tagNET_DVR_SENSOR_ADJUSTMENT, [
    ('dwSize', DWORD),
    ('byType', BYTE),
    ('bySensorNo', BYTE),
    ('byRes', BYTE * 2),
    ('iAdjustMentRange', c_int),
    ('byR', BYTE),
    ('byG', BYTE),
    ('byB', BYTE),
    ('byRgbType', BYTE),
    ('byBrightness', BYTE),
    ('byRes1', BYTE * 3),
    ('wRex', WORD),
    ('wGex', WORD),
    ('wBex', WORD),
    ('byRes2', BYTE * 114),
])

NET_DVR_SENSOR_ADJUSTMENT = struct_tagNET_DVR_SENSOR_ADJUSTMENT
LPNET_DVR_SENSOR_ADJUSTMENT = POINTER(struct_tagNET_DVR_SENSOR_ADJUSTMENT)
tagNET_DVR_SENSOR_ADJUSTMENT = struct_tagNET_DVR_SENSOR_ADJUSTMENT
