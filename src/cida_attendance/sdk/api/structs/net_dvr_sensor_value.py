from ctypes import Structure, c_float

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SENSOR_VALUE(Structure):
    pass

_S(struct_tagNET_DVR_SENSOR_VALUE, [
    ('fMinValue', c_float),
    ('fMaxValue', c_float),
    ('byRes', BYTE * 8),
])

NET_DVR_SENSOR_VALUE = struct_tagNET_DVR_SENSOR_VALUE
LPNET_DVR_SENSOR_VALUE = POINTER(struct_tagNET_DVR_SENSOR_VALUE)
tagNET_DVR_SENSOR_VALUE = struct_tagNET_DVR_SENSOR_VALUE
