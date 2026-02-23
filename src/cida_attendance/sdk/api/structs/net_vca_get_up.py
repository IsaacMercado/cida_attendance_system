from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .net_vca_polygon import NET_VCA_POLYGON


class struct_tagNET_VCA_GET_UP(Structure):
    pass

_S(struct_tagNET_VCA_GET_UP, [
    ('struRegion', NET_VCA_POLYGON),
    ('wDuration', WORD),
    ('byMode', BYTE),
    ('bySensitivity', BYTE),
    ('byRes', BYTE * 4),
])

NET_VCA_GET_UP = struct_tagNET_VCA_GET_UP
LPNET_VCA_GET_UP = POINTER(struct_tagNET_VCA_GET_UP)
tagNET_VCA_GET_UP = struct_tagNET_VCA_GET_UP
