from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_vca_polygon import NET_VCA_POLYGON


class struct_tagNET_VCA_MASK_REGION(Structure):
    pass

_S(struct_tagNET_VCA_MASK_REGION, [
    ('byEnable', BYTE),
    ('byRes', BYTE * 3),
    ('struPolygon', NET_VCA_POLYGON),
])

NET_VCA_MASK_REGION = struct_tagNET_VCA_MASK_REGION
LPNET_VCA_MASK_REGION = POINTER(struct_tagNET_VCA_MASK_REGION)
tagNET_VCA_MASK_REGION = struct_tagNET_VCA_MASK_REGION
