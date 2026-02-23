from ctypes import Structure, c_char, c_float

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .net_vca_point import NET_VCA_POINT
from .net_vca_polygon import NET_VCA_POLYGON


class struct_tagNET_DVR_THERMOMETRY_PRESETINFO_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_THERMOMETRY_PRESETINFO_PARAM, [
    ('byEnabled', BYTE),
    ('byRuleID', BYTE),
    ('wDistance', WORD),
    ('fEmissivity', c_float),
    ('byDistanceUnit', BYTE),
    ('byRes', BYTE * 2),
    ('byReflectiveEnabled', BYTE),
    ('fReflectiveTemperature', c_float),
    ('szRuleName', c_char * 32),
    ('byemissivityMode', BYTE),
    ('byRes1', BYTE * 62),
    ('byRuleCalibType', BYTE),
    ('struPoint', NET_VCA_POINT),
    ('struRegion', NET_VCA_POLYGON),
])

NET_DVR_THERMOMETRY_PRESETINFO_PARAM = struct_tagNET_DVR_THERMOMETRY_PRESETINFO_PARAM
LPNET_DVR_THERMOMETRY_PRESETINFO_PARAM = POINTER(struct_tagNET_DVR_THERMOMETRY_PRESETINFO_PARAM)
tagNET_DVR_THERMOMETRY_PRESETINFO_PARAM = struct_tagNET_DVR_THERMOMETRY_PRESETINFO_PARAM
