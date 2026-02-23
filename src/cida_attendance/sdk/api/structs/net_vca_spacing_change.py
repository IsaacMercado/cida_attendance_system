from ctypes import Structure, c_float

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .net_vca_polygon import NET_VCA_POLYGON


class struct_tagNET_VCA_SPACING_CHANGE(Structure):
    pass

_S(struct_tagNET_VCA_SPACING_CHANGE, [
    ('struRegion', NET_VCA_POLYGON),
    ('fSpacingThreshold', c_float),
    ('bySensitivity', BYTE),
    ('byDetectMode', BYTE),
    ('wDuration', WORD),
])

NET_VCA_SPACING_CHANGE = struct_tagNET_VCA_SPACING_CHANGE
LPNET_VCA_SPACING_CHANGE = POINTER(struct_tagNET_VCA_SPACING_CHANGE)
tagNET_VCA_SPACING_CHANGE = struct_tagNET_VCA_SPACING_CHANGE
