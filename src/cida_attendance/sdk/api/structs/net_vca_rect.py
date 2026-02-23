from ctypes import Structure, c_float

from ..base_classes import _S
from ..ctypes_preamble import POINTER


class struct_tagNET_VCA_RECT(Structure):
    pass

_S(struct_tagNET_VCA_RECT, [
    ('fX', c_float),
    ('fY', c_float),
    ('fWidth', c_float),
    ('fHeight', c_float),
])

NET_VCA_RECT = struct_tagNET_VCA_RECT
LPNET_VCA_RECT = POINTER(struct_tagNET_VCA_RECT)
tagNET_VCA_RECT = struct_tagNET_VCA_RECT
