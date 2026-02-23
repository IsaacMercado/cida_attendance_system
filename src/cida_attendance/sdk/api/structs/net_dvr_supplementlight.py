from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .anon_386 import NET_DVR_SCHEDULE_DAYTIME


class struct_tagNET_DVR_SUPPLEMENTLIGHT(Structure):
    pass

_S(struct_tagNET_DVR_SUPPLEMENTLIGHT, [
    ('byEnable', BYTE),
    ('byMode', BYTE),
    ('byHighBeamBrightness', BYTE),
    ('byLowBeamBrightness', BYTE),
    ('struSchedTime', NET_DVR_SCHEDULE_DAYTIME),
    ('wFilteringTime', WORD),
    ('byBrightness', BYTE),
    ('bySensitivity', BYTE),
    ('byBrightnessRegulatMode', BYTE),
    ('byMaxBrightness', BYTE),
    ('byRes', BYTE * 58),
])

NET_DVR_SUPPLEMENTLIGHT = struct_tagNET_DVR_SUPPLEMENTLIGHT
LPNET_DVR_SUPPLEMENTLIGHT = POINTER(struct_tagNET_DVR_SUPPLEMENTLIGHT)
tagNET_DVR_SUPPLEMENTLIGHT = struct_tagNET_DVR_SUPPLEMENTLIGHT
