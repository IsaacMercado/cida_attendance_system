from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .net_vca_polygon import NET_VCA_POLYGON


class struct_tagNET_VCA_TAKE(Structure):
    pass

_S(struct_tagNET_VCA_TAKE, [
    ('struRegion', NET_VCA_POLYGON),
    ('wDuration', WORD),
    ('bySensitivity', BYTE),
    ('byRes', BYTE * 5),
])

NET_VCA_TAKE = struct_tagNET_VCA_TAKE
LPNET_VCA_TAKE = POINTER(struct_tagNET_VCA_TAKE)
tagNET_VCA_TAKE = struct_tagNET_VCA_TAKE
