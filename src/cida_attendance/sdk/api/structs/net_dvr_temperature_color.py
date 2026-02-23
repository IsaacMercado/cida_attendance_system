from ctypes import Structure, c_int

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_TEMPERATURE_COLOR(Structure):
    pass

_S(struct_tagNET_DVR_TEMPERATURE_COLOR, [
    ('byType', BYTE),
    ('byRes1', BYTE * 3),
    ('iHighTemperature', c_int),
    ('iLowTemperature', c_int),
    ('byRes', BYTE * 8),
])

NET_DVR_TEMPERATURE_COLOR = struct_tagNET_DVR_TEMPERATURE_COLOR
LPNET_DVR_TEMPERATURE_COLOR = POINTER(struct_tagNET_DVR_TEMPERATURE_COLOR)
tagNET_DVR_TEMPERATURE_COLOR = struct_tagNET_DVR_TEMPERATURE_COLOR
