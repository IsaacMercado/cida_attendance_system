from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from ..enums import VCA_CROSS_DIRECTION
from .net_vca_line import NET_VCA_LINE


class struct_tagNET_VCA_TRAVERSE_PLANE(Structure):
    pass

_S(struct_tagNET_VCA_TRAVERSE_PLANE, [
    ('struPlaneBottom', NET_VCA_LINE),
    ('dwCrossDirection', VCA_CROSS_DIRECTION),
    ('bySensitivity', BYTE),
    ('byPlaneHeight', BYTE),
    ('byDetectionTarget', BYTE),
    ('byPriority', BYTE),
    ('byAlarmConfidence', BYTE),
    ('byRecordConfidence', BYTE),
    ('byRes2', BYTE * 34),
])

NET_VCA_TRAVERSE_PLANE = struct_tagNET_VCA_TRAVERSE_PLANE
LPNET_VCA_TRAVERSE_PLANE = POINTER(struct_tagNET_VCA_TRAVERSE_PLANE)
tagNET_VCA_TRAVERSE_PLANE = struct_tagNET_VCA_TRAVERSE_PLANE
