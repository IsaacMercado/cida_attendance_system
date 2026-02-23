from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .net_vca_polygon import NET_VCA_POLYGON


class struct_tagNET_VCA_TAKE_LEFT(Structure):
    pass

_S(struct_tagNET_VCA_TAKE_LEFT, [
    ('struRegion', NET_VCA_POLYGON),
    ('wDuration', WORD),
    ('bySensitivity', BYTE),
    ('byRes', BYTE * 5),
])

NET_VCA_TAKE_LEFT = struct_tagNET_VCA_TAKE_LEFT
LPNET_VCA_TAKE_LEFT = POINTER(struct_tagNET_VCA_TAKE_LEFT)
tagNET_VCA_TAKE_LEFT = struct_tagNET_VCA_TAKE_LEFT
