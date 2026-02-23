from ctypes import Structure, c_float

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_vca_polygon import NET_VCA_POLYGON


class struct_tagNET_VCA_HIGH_DENSITY_STATUS(Structure):
    pass

_S(struct_tagNET_VCA_HIGH_DENSITY_STATUS, [
    ('struRegion', NET_VCA_POLYGON),
    ('fDensity', c_float),
    ('bySensitivity', BYTE),
    ('byRes', BYTE * 3),
])

NET_VCA_HIGH_DENSITY_STATUS = struct_tagNET_VCA_HIGH_DENSITY_STATUS
LPNET_VCA_HIGH_DENSITY_STATUS = POINTER(struct_tagNET_VCA_HIGH_DENSITY_STATUS)
tagNET_VCA_HIGH_DENSITY_STATUS = struct_tagNET_VCA_HIGH_DENSITY_STATUS
