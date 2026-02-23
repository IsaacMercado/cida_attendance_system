from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_vca_polygon import NET_VCA_POLYGON


class struct_tagNET_VCA_AREA(Structure):
    pass

_S(struct_tagNET_VCA_AREA, [
    ('struRegion', NET_VCA_POLYGON),
    ('bySensitivity', BYTE),
    ('byDetectionTarget', BYTE),
    ('byPriority', BYTE),
    ('byRes', BYTE * 5),
])

NET_VCA_AREA = struct_tagNET_VCA_AREA
LPNET_VCA_AREA = POINTER(struct_tagNET_VCA_AREA)
tagNET_VCA_AREA = struct_tagNET_VCA_AREA
