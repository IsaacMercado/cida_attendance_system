from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .net_vca_polygon import NET_VCA_POLYGON


class struct_tagNET_VCA_TRAIL(Structure):
    pass

_S(struct_tagNET_VCA_TRAIL, [
    ('struRegion', NET_VCA_POLYGON),
    ('wRes', WORD),
    ('bySensitivity', BYTE),
    ('byRes', BYTE * 5),
])

NET_VCA_TRAIL = struct_tagNET_VCA_TRAIL
LPNET_VCA_TRAIL = POINTER(struct_tagNET_VCA_TRAIL)
tagNET_VCA_TRAIL = struct_tagNET_VCA_TRAIL
