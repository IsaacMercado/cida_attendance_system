from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_polygon import NET_VCA_POLYGON


class struct_tagNET_VCA_ADV_TRAVERSE_PLANE(Structure):
    pass

_S(struct_tagNET_VCA_ADV_TRAVERSE_PLANE, [
    ('struRegion', NET_VCA_POLYGON),
    ('dwCrossDirection', DWORD),
    ('bySensitivity', BYTE),
    ('byRes', BYTE * 3),
])

NET_VCA_ADV_TRAVERSE_PLANE = struct_tagNET_VCA_ADV_TRAVERSE_PLANE
LPNET_VCA_ADV_TRAVERSE_PLANE = POINTER(struct_tagNET_VCA_ADV_TRAVERSE_PLANE)
tagNET_VCA_ADV_TRAVERSE_PLANE = struct_tagNET_VCA_ADV_TRAVERSE_PLANE
