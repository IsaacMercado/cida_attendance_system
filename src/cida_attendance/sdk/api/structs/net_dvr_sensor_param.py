from ctypes import Structure, c_float

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SENSOR_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_SENSOR_PARAM, [
    ('bySensorType', BYTE),
    ('byRes', BYTE * 31),
    ('fHorWidth', c_float),
    ('fVerWidth', c_float),
    ('fFold', c_float),
])

NET_DVR_SENSOR_PARAM = struct_tagNET_DVR_SENSOR_PARAM
LPNET_DVR_SENSOR_PARAM = POINTER(struct_tagNET_DVR_SENSOR_PARAM)
tagNET_DVR_SENSOR_PARAM = struct_tagNET_DVR_SENSOR_PARAM
