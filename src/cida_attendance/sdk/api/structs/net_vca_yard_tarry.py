from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .net_vca_polygon import NET_VCA_POLYGON


class struct_tagNET_VCA_YARD_TARRY(Structure):
    pass

_S(struct_tagNET_VCA_YARD_TARRY, [
    ('struRegion', NET_VCA_POLYGON),
    ('wDelay', WORD),
    ('byRes', BYTE * 6),
])

NET_VCA_YARD_TARRY = struct_tagNET_VCA_YARD_TARRY
LPNET_VCA_YARD_TARRY = POINTER(struct_tagNET_VCA_YARD_TARRY)
tagNET_VCA_YARD_TARRY = struct_tagNET_VCA_YARD_TARRY
