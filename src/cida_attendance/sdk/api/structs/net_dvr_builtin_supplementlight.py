from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_386 import NET_DVR_SCHEDULE_DAYTIME


class struct_tagNET_DVR_BUILTIN_SUPPLEMENTLIGHT(Structure):
    pass

_S(struct_tagNET_DVR_BUILTIN_SUPPLEMENTLIGHT, [
    ('dwSize', DWORD),
    ('byMode', BYTE),
    ('byBrightnessLimit', BYTE),
    ('bySupplementLightMode', BYTE),
    ('byMixedLightRegulatMode', BYTE),
    ('byLrLightBrightness', BYTE),
    ('byHighLrLightBrightness', BYTE),
    ('byHighBrightnessLimit', BYTE),
    ('byLowLrLightBrightness', BYTE),
    ('struSchedTime', NET_DVR_SCHEDULE_DAYTIME),
    ('byLowBrightnessLimit', BYTE),
    ('byWhiteLightBrightness', BYTE),
    ('byIrLightbrightnessLimit', BYTE),
    ('byWhiteLightbrightnessLimit', BYTE),
    ('byRes1', BYTE * 252),
])

NET_DVR_BUILTIN_SUPPLEMENTLIGHT = struct_tagNET_DVR_BUILTIN_SUPPLEMENTLIGHT
LPNET_DVR_BUILTIN_SUPPLEMENTLIGHT = POINTER(struct_tagNET_DVR_BUILTIN_SUPPLEMENTLIGHT)
tagNET_DVR_BUILTIN_SUPPLEMENTLIGHT = struct_tagNET_DVR_BUILTIN_SUPPLEMENTLIGHT
