from ctypes import Structure, c_float

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_vca_point import NET_VCA_POINT


class struct_tagNET_DVR_POINT_THERM_CFG(Structure):
    pass

_S(struct_tagNET_DVR_POINT_THERM_CFG, [
    ('fTemperature', c_float),
    ('struPoint', NET_VCA_POINT),
    ('byRes', BYTE * 120),
])

NET_DVR_POINT_THERM_CFG = struct_tagNET_DVR_POINT_THERM_CFG
LPNET_DVR_POINT_THERM_CFG = POINTER(struct_tagNET_DVR_POINT_THERM_CFG)
tagNET_DVR_POINT_THERM_CFG = struct_tagNET_DVR_POINT_THERM_CFG
