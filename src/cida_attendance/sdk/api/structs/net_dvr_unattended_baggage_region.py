from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .net_vca_polygon import NET_VCA_POLYGON


class struct_tagNET_DVR_UNATTENDED_BAGGAGE_REGION(Structure):
    pass

_S(struct_tagNET_DVR_UNATTENDED_BAGGAGE_REGION, [
    ('struRegion', NET_VCA_POLYGON),
    ('bySensitivity', BYTE),
    ('byTimeThreshold', BYTE),
    ('wTimeThreshold', WORD),
    ('byTimeThresholdMode', BYTE),
    ('byRes', BYTE * 59),
])

NET_DVR_UNATTENDED_BAGGAGE_REGION = struct_tagNET_DVR_UNATTENDED_BAGGAGE_REGION
LPNET_DVR_UNATTENDED_BAGGAGE_REGION = POINTER(struct_tagNET_DVR_UNATTENDED_BAGGAGE_REGION)
tagNET_DVR_UNATTENDED_BAGGAGE_REGION = struct_tagNET_DVR_UNATTENDED_BAGGAGE_REGION
