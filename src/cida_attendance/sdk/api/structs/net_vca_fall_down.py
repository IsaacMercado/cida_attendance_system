from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .net_vca_polygon import NET_VCA_POLYGON


class struct_tagNET_VCA_FALL_DOWN(Structure):
    pass

_S(struct_tagNET_VCA_FALL_DOWN, [
    ('struRegion', NET_VCA_POLYGON),
    ('wDuration', WORD),
    ('bySensitivity', BYTE),
    ('byHeightThreshold', BYTE),
    ('byRes', BYTE * 4),
])

NET_VCA_FALL_DOWN = struct_tagNET_VCA_FALL_DOWN
LPNET_VCA_FALL_DOWN = POINTER(struct_tagNET_VCA_FALL_DOWN)
tagNET_VCA_FALL_DOWN = struct_tagNET_VCA_FALL_DOWN
