from ctypes import Structure, c_float

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_vca_polygon import NET_VCA_POLYGON


class struct_tagNET_DVR_LINEPOLYGON_THERM_CFG(Structure):
    pass

_S(struct_tagNET_DVR_LINEPOLYGON_THERM_CFG, [
    ('fMaxTemperature', c_float),
    ('fMinTemperature', c_float),
    ('fAverageTemperature', c_float),
    ('fTemperatureDiff', c_float),
    ('struRegion', NET_VCA_POLYGON),
    ('byRes', BYTE * 32),
])

NET_DVR_LINEPOLYGON_THERM_CFG = struct_tagNET_DVR_LINEPOLYGON_THERM_CFG
LPNET_DVR_LINEPOLYGON_THERM_CFG = POINTER(struct_tagNET_DVR_LINEPOLYGON_THERM_CFG)
tagNET_DVR_LINEPOLYGON_THERM_CFG = struct_tagNET_DVR_LINEPOLYGON_THERM_CFG
