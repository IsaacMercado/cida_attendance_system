from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_vca_polygon import NET_VCA_POLYGON


class struct_tagNET_DVR_RAPIDMOVE_REGION(Structure):
    pass

_S(struct_tagNET_DVR_RAPIDMOVE_REGION, [
    ('struRegion', NET_VCA_POLYGON),
    ('bySensitivity', BYTE),
    ('byDetectionTarget', BYTE),
    ('byRes', BYTE * 62),
])

NET_DVR_RAPIDMOVE_REGION = struct_tagNET_DVR_RAPIDMOVE_REGION
LPNET_DVR_RAPIDMOVE_REGION = POINTER(struct_tagNET_DVR_RAPIDMOVE_REGION)
tagNET_DVR_RAPIDMOVE_REGION = struct_tagNET_DVR_RAPIDMOVE_REGION
