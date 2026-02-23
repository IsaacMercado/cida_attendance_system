from ctypes import Structure, c_float

from ..base_classes import _S
from ..ctypes_preamble import POINTER


class struct_tagNET_VCA_POINT(Structure):
    pass

_S(struct_tagNET_VCA_POINT, [
    ('fX', c_float),
    ('fY', c_float),
])

NET_VCA_POINT = struct_tagNET_VCA_POINT
LPNET_VCA_POINT = POINTER(struct_tagNET_VCA_POINT)
tagNET_VCA_POINT = struct_tagNET_VCA_POINT
