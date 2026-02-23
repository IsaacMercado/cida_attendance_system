from ctypes import Structure, c_float, c_int

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_ITC_RADAR_PARAM(Structure):
    pass

_S(struct_tagNET_ITC_RADAR_PARAM, [
    ('byRadarType', BYTE),
    ('byLevelAngle', BYTE),
    ('wRadarSensitivity', WORD),
    ('wRadarSpeedValidTime', WORD),
    ('byRes1', BYTE * 2),
    ('fLineCorrectParam', c_float),
    ('iConstCorrectParam', c_int),
    ('byRes2', BYTE * 8),
])

NET_ITC_RADAR_PARAM = struct_tagNET_ITC_RADAR_PARAM
LPNET_ITC_RADAR_PARAM = POINTER(struct_tagNET_ITC_RADAR_PARAM)
tagNET_ITC_RADAR_PARAM = struct_tagNET_ITC_RADAR_PARAM
