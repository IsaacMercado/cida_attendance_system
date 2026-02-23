from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_26 import NET_DVR_COLOR


class struct_tagNET_DVR_DISPLAY_EFFECT_CFG(Structure):
    pass

_S(struct_tagNET_DVR_DISPLAY_EFFECT_CFG, [
    ('dwSize', DWORD),
    ('struColor', NET_DVR_COLOR),
    ('byRes', BYTE * 32),
])

NET_DVR_DISPLAY_EFFECT_CFG = struct_tagNET_DVR_DISPLAY_EFFECT_CFG
LPNET_DVR_DISPLAY_EFFECT_CFG = POINTER(struct_tagNET_DVR_DISPLAY_EFFECT_CFG)
tagNET_DVR_DISPLAY_EFFECT_CFG = struct_tagNET_DVR_DISPLAY_EFFECT_CFG
