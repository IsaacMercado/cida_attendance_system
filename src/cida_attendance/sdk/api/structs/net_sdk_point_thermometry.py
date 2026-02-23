from ctypes import Structure, c_float

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_vca_point import NET_VCA_POINT


class struct_tagNET_SDK_POINT_THERMOMETRY(Structure):
    pass

_S(struct_tagNET_SDK_POINT_THERMOMETRY, [
    ('fPointTemperature', c_float),
    ('struPoint', NET_VCA_POINT),
    ('byRes', BYTE * 20),
])

NET_SDK_POINT_THERMOMETRY = struct_tagNET_SDK_POINT_THERMOMETRY
LPNET_SDK_POINT_THERMOMETRY = POINTER(struct_tagNET_SDK_POINT_THERMOMETRY)
tagNET_SDK_POINT_THERMOMETRY = struct_tagNET_SDK_POINT_THERMOMETRY
