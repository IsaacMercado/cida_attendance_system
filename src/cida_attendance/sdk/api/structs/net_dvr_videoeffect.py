from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_VIDEOEFFECT(Structure):
    pass

_S(struct_tagNET_DVR_VIDEOEFFECT, [
    ('byBrightnessLevel', BYTE),
    ('byContrastLevel', BYTE),
    ('bySharpnessLevel', BYTE),
    ('bySaturationLevel', BYTE),
    ('byHueLevel', BYTE),
    ('byEnableFunc', BYTE),
    ('byLightInhibitLevel', BYTE),
    ('byGrayLevel', BYTE),
])

NET_DVR_VIDEOEFFECT = struct_tagNET_DVR_VIDEOEFFECT
LPNET_DVR_VIDEOEFFECT = POINTER(struct_tagNET_DVR_VIDEOEFFECT)
tagNET_DVR_VIDEOEFFECT = struct_tagNET_DVR_VIDEOEFFECT
