from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_27 import NET_DVR_RGB_COLOR
from .net_dvr_videoeffect import NET_DVR_VIDEOEFFECT


class struct_tagNET_DVR_WALLOUTPUTPARAM(Structure):
    pass

_S(struct_tagNET_DVR_WALLOUTPUTPARAM, [
    ('dwSize', DWORD),
    ('dwResolution', DWORD),
    ('struRes', NET_DVR_VIDEOEFFECT),
    ('byVideoFormat', BYTE),
    ('byDisplayMode', BYTE),
    ('byBackgroundColor', BYTE),
    ('byUseEDIDResolution', BYTE),
    ('wLEDWidth', WORD),
    ('wLEDHeight', WORD),
    ('struBackColor', NET_DVR_RGB_COLOR),
    ('byLinkStatus', BYTE),
    ('byRes2', BYTE * 51),
])

NET_DVR_WALLOUTPUTPARAM = struct_tagNET_DVR_WALLOUTPUTPARAM
LPNET_DVR_WALLOUTPUTPARAM = POINTER(struct_tagNET_DVR_WALLOUTPUTPARAM)
tagNET_DVR_WALLOUTPUTPARAM = struct_tagNET_DVR_WALLOUTPUTPARAM
