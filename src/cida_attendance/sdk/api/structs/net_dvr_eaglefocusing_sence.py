from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .net_vca_polygon import NET_VCA_POLYGON


class struct_tagNET_DVR_EAGLEFOCUSING_SENCE(Structure):
    pass

_S(struct_tagNET_DVR_EAGLEFOCUSING_SENCE, [
    ('byRuleType', BYTE),
    ('bySceneID', BYTE),
    ('wRate', WORD),
    ('struRegion', NET_VCA_POLYGON),
    ('bySpotNum', BYTE),
    ('byRes', BYTE * 127),
])

NET_DVR_EAGLEFOCUSING_SENCE = struct_tagNET_DVR_EAGLEFOCUSING_SENCE
LPNET_DVR_EAGLEFOCUSING_SENCE = POINTER(struct_tagNET_DVR_EAGLEFOCUSING_SENCE)
tagNET_DVR_EAGLEFOCUSING_SENCE = struct_tagNET_DVR_EAGLEFOCUSING_SENCE
