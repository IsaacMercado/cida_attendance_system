from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .net_vca_polygon import NET_VCA_POLYGON


class struct_tagNET_VCA_LECTURE(Structure):
    pass

_S(struct_tagNET_VCA_LECTURE, [
    ('struRegion', NET_VCA_POLYGON),
    ('wDuration', WORD),
    ('bySensitivity', BYTE),
    ('byAlarmState', BYTE),
    ('byTrackingMode', BYTE),
    ('byZoomMode', BYTE),
    ('byZoomOver', BYTE),
    ('byTrackStatus', BYTE),
])

NET_VCA_LECTURE = struct_tagNET_VCA_LECTURE
LPNET_VCA_LECTURE = POINTER(struct_tagNET_VCA_LECTURE)
tagNET_VCA_LECTURE = struct_tagNET_VCA_LECTURE
