from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_vca_polygon import NET_VCA_POLYGON


class struct_tagNET_DVR_TRACKING(Structure):
    pass

_S(struct_tagNET_DVR_TRACKING, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byMode', BYTE),
    ('wTrackingTime', WORD),
    ('struRegion', NET_VCA_POLYGON),
    ('byRes', BYTE * 64),
])

NET_DVR_TRACKING = struct_tagNET_DVR_TRACKING
LPNET_DVR_TRACKING = POINTER(struct_tagNET_DVR_TRACKING)
tagNET_DVR_TRACKING = struct_tagNET_DVR_TRACKING
