from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .net_vca_polygon import NET_VCA_POLYGON


class struct_tagNET_VCA_OVER_TIME(Structure):
    pass

_S(struct_tagNET_VCA_OVER_TIME, [
    ('struRegion', NET_VCA_POLYGON),
    ('wDuration', WORD),
    ('byRes', BYTE * 6),
])

NET_VCA_OVER_TIME = struct_tagNET_VCA_OVER_TIME
LPNET_VCA_OVER_TIME = POINTER(struct_tagNET_VCA_OVER_TIME)
tagNET_VCA_OVER_TIME = struct_tagNET_VCA_OVER_TIME
