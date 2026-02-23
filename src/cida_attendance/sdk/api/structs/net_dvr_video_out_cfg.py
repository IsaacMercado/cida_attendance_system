from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_VIDEO_OUT_CFG(Structure):
    pass

_S(struct_tagNET_DVR_VIDEO_OUT_CFG, [
    ('byDisplayMode', BYTE),
    ('byBrightnessLevel', BYTE),
    ('byContrastLevel', BYTE),
    ('bySharpnessLevel', BYTE),
    ('bySaturationLevel', BYTE),
    ('byHueLevel', BYTE),
    ('byImageMode', BYTE),
    ('byRes', BYTE * 5),
])

NET_DVR_VIDEO_OUT_CFG = struct_tagNET_DVR_VIDEO_OUT_CFG
LPNET_DVR_VIDEO_OUT_CFG = POINTER(struct_tagNET_DVR_VIDEO_OUT_CFG)
tagNET_DVR_VIDEO_OUT_CFG = struct_tagNET_DVR_VIDEO_OUT_CFG
