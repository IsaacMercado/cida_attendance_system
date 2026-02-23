from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_VIDEO_EFFECT(Structure):
    pass

_S(struct_tagNET_DVR_VIDEO_EFFECT, [
    ('dwBrightValue', DWORD),
    ('dwContrastValue', DWORD),
    ('dwSaturationValue', DWORD),
    ('dwHueValue', DWORD),
    ('dwSharpness', DWORD),
    ('dwDenoising', DWORD),
    ('byRes', BYTE * 12),
])

NET_DVR_VIDEO_EFFECT = struct_tagNET_DVR_VIDEO_EFFECT
LPNET_DVR_VIDEO_EFFECT = POINTER(struct_tagNET_DVR_VIDEO_EFFECT)
tagNET_DVR_VIDEO_EFFECT = struct_tagNET_DVR_VIDEO_EFFECT
