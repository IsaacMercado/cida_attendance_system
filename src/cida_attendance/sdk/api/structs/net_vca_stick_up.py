from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .net_vca_polygon import NET_VCA_POLYGON


class struct_tagNET_VCA_STICK_UP(Structure):
    pass

_S(struct_tagNET_VCA_STICK_UP, [
    ('struRegion', NET_VCA_POLYGON),
    ('wDuration', WORD),
    ('bySensitivity', BYTE),
    ('byRes', BYTE * 5),
])

NET_VCA_STICK_UP = struct_tagNET_VCA_STICK_UP
LPNET_VCA_STICK_UP = POINTER(struct_tagNET_VCA_STICK_UP)
tagNET_VCA_STICK_UP = struct_tagNET_VCA_STICK_UP
