from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_polygon import NET_VCA_POLYGON


class struct_tagNET_VCA_ENTER_REGION(Structure):
    pass

_S(struct_tagNET_VCA_ENTER_REGION, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byRes1', BYTE * 3),
    ('struPolygon', NET_VCA_POLYGON),
    ('byRes2', BYTE * 16),
])

NET_VCA_ENTER_REGION = struct_tagNET_VCA_ENTER_REGION
LPNET_VCA_ENTER_REGION = POINTER(struct_tagNET_VCA_ENTER_REGION)
tagNET_VCA_ENTER_REGION = struct_tagNET_VCA_ENTER_REGION
