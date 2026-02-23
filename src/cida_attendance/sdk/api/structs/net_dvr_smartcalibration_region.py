from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_vca_polygon import NET_VCA_POLYGON


class struct_tagNET_DVR_SMARTCALIBRATION_REGION(Structure):
    pass

_S(struct_tagNET_DVR_SMARTCALIBRATION_REGION, [
    ('byRuleID', BYTE),
    ('byMode', BYTE),
    ('byStrategy', BYTE),
    ('byPriority', BYTE),
    ('struMaxTargetSize', NET_VCA_POLYGON),
    ('struMinTargetSize', NET_VCA_POLYGON),
])

NET_DVR_SMARTCALIBRATION_REGION = struct_tagNET_DVR_SMARTCALIBRATION_REGION
LPNET_DVR_SMARTCALIBRATION_REGION = POINTER(struct_tagNET_DVR_SMARTCALIBRATION_REGION)
tagNET_DVR_SMARTCALIBRATION_REGION = struct_tagNET_DVR_SMARTCALIBRATION_REGION
