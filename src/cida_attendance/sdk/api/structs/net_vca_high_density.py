from ctypes import Structure, c_float

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .net_vca_polygon import NET_VCA_POLYGON


class struct_tagNET_VCA_HIGH_DENSITY(Structure):
    pass

_S(struct_tagNET_VCA_HIGH_DENSITY, [
    ('struRegion', NET_VCA_POLYGON),
    ('fDensity', c_float),
    ('bySensitivity', BYTE),
    ('byRes', BYTE),
    ('wDuration', WORD),
])

NET_VCA_HIGH_DENSITY = struct_tagNET_VCA_HIGH_DENSITY
LPNET_VCA_HIGH_DENSITY = POINTER(struct_tagNET_VCA_HIGH_DENSITY)
tagNET_VCA_HIGH_DENSITY = struct_tagNET_VCA_HIGH_DENSITY
