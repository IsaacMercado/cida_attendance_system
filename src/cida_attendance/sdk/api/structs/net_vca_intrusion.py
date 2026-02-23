from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .net_vca_polygon import NET_VCA_POLYGON


class struct_tagNET_VCA_INTRUSION(Structure):
    pass

_S(struct_tagNET_VCA_INTRUSION, [
    ('struRegion', NET_VCA_POLYGON),
    ('wDuration', WORD),
    ('bySensitivity', BYTE),
    ('byRate', BYTE),
    ('byDetectionTarget', BYTE),
    ('byPriority', BYTE),
    ('byAlarmConfidence', BYTE),
    ('byRecordConfidence', BYTE),
])

NET_VCA_INTRUSION = struct_tagNET_VCA_INTRUSION
LPNET_VCA_INTRUSION = POINTER(struct_tagNET_VCA_INTRUSION)
tagNET_VCA_INTRUSION = struct_tagNET_VCA_INTRUSION
