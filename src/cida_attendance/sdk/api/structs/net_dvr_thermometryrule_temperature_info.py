from ctypes import Structure, c_float

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_vca_point import NET_VCA_POINT


class struct_tagNET_DVR_THERMOMETRYRULE_TEMPERATURE_INFO(Structure):
    pass

_S(struct_tagNET_DVR_THERMOMETRYRULE_TEMPERATURE_INFO, [
    ('fMaxTemperature', c_float),
    ('fMinTemperature', c_float),
    ('fAverageTemperature', c_float),
    ('struHighestPoint', NET_VCA_POINT),
    ('struLowestPoint', NET_VCA_POINT),
    ('byIsFreezedata', BYTE),
    ('byRes', BYTE * 15),
])

NET_DVR_THERMOMETRYRULE_TEMPERATURE_INFO = struct_tagNET_DVR_THERMOMETRYRULE_TEMPERATURE_INFO
LPNET_DVR_THERMOMETRYRULE_TEMPERATURE_INFO = POINTER(struct_tagNET_DVR_THERMOMETRYRULE_TEMPERATURE_INFO)
tagNET_DVR_THERMOMETRYRULE_TEMPERATURE_INFO = struct_tagNET_DVR_THERMOMETRYRULE_TEMPERATURE_INFO
