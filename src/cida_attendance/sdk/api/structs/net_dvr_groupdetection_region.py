from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_vca_polygon import NET_VCA_POLYGON


class struct_tagNET_DVR_GROUPDETECTION_REGION(Structure):
    pass

_S(struct_tagNET_DVR_GROUPDETECTION_REGION, [
    ('struRegion', NET_VCA_POLYGON),
    ('byObjectOccup', BYTE),
    ('bySensitivityLevel', BYTE),
    ('byDurationTime', BYTE),
    ('byFilterTime', BYTE),
    ('byMinTriggerNumber', BYTE),
    ('byLinkageTime', BYTE),
    ('byRes', BYTE * 58),
])

NET_DVR_GROUPDETECTION_REGION = struct_tagNET_DVR_GROUPDETECTION_REGION
LPNET_DVR_GROUPDETECTION_REGION = POINTER(struct_tagNET_DVR_GROUPDETECTION_REGION)
tagNET_DVR_GROUPDETECTION_REGION = struct_tagNET_DVR_GROUPDETECTION_REGION
