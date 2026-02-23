from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ACS_SCREEN_DISPLAY_CFG(Structure):
    pass

_S(struct_tagNET_DVR_ACS_SCREEN_DISPLAY_CFG, [
    ('dwSize', DWORD),
    ('dwFontSize', DWORD),
    ('dwRowSpacing', DWORD),
    ('dwColumnSpacing', DWORD),
    ('dwFirstRowPosition', DWORD),
    ('byDegree', BYTE),
    ('byScreenType', BYTE),
    ('byRes', BYTE * 306),
])

NET_DVR_ACS_SCREEN_DISPLAY_CFG = struct_tagNET_DVR_ACS_SCREEN_DISPLAY_CFG
LPNET_DVR_ACS_SCREEN_DISPLAY_CFG = POINTER(struct_tagNET_DVR_ACS_SCREEN_DISPLAY_CFG)
tagNET_DVR_ACS_SCREEN_DISPLAY_CFG = struct_tagNET_DVR_ACS_SCREEN_DISPLAY_CFG
