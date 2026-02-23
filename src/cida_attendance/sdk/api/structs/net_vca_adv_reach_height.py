from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_polygon import NET_VCA_POLYGON


class struct_tagNET_VCA_ADV_REACH_HEIGHT(Structure):
    pass

_S(struct_tagNET_VCA_ADV_REACH_HEIGHT, [
    ('struRegion', NET_VCA_POLYGON),
    ('dwCrossDirection', DWORD),
    ('byRes', BYTE * 4),
])

NET_VCA_ADV_REACH_HEIGHT = struct_tagNET_VCA_ADV_REACH_HEIGHT
LPNET_VCA_ADV_REACH_HEIGHT = POINTER(struct_tagNET_VCA_ADV_REACH_HEIGHT)
tagNET_VCA_ADV_REACH_HEIGHT = struct_tagNET_VCA_ADV_REACH_HEIGHT
