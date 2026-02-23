from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .net_vca_polygon import NET_VCA_POLYGON


class struct_tagNET_VCA_PARKING(Structure):
    pass

_S(struct_tagNET_VCA_PARKING, [
    ('struRegion', NET_VCA_POLYGON),
    ('wDuration', WORD),
    ('bySensitivity', BYTE),
    ('byRes', BYTE * 5),
])

NET_VCA_PARKING = struct_tagNET_VCA_PARKING
LPNET_VCA_PARKING = POINTER(struct_tagNET_VCA_PARKING)
tagNET_VCA_PARKING = struct_tagNET_VCA_PARKING
