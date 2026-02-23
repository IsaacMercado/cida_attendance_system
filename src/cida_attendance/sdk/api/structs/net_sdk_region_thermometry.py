from ctypes import Structure, c_float

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_vca_polygon import NET_VCA_POLYGON


class struct_tagNET_SDK_REGION_THERMOMETRY(Structure):
    pass

_S(struct_tagNET_SDK_REGION_THERMOMETRY, [
    ('fMaxTemperature', c_float),
    ('fMinTemperature', c_float),
    ('fAverageTemperature', c_float),
    ('fTemperatureDiff', c_float),
    ('struRegion', NET_VCA_POLYGON),
    ('byRes', BYTE * 20),
])

NET_SDK_REGION_THERMOMETRY = struct_tagNET_SDK_REGION_THERMOMETRY
LPNET_SDK_REGION_THERMOMETRY = POINTER(struct_tagNET_SDK_REGION_THERMOMETRY)
tagNET_SDK_REGION_THERMOMETRY = struct_tagNET_SDK_REGION_THERMOMETRY
