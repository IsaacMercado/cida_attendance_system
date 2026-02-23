from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_LED_SCREEN_CFG(Structure):
    pass

_S(struct_tagNET_DVR_LED_SCREEN_CFG, [
    ('dwSize', DWORD),
    ('sLEDName', BYTE * 32),
    ('byTransMode', BYTE),
    ('byProtocolType', BYTE),
    ('byLEDColor', BYTE),
    ('byDataPolarity', BYTE),
    ('byOEPolarity', BYTE),
    ('byScanMode', BYTE),
    ('byRes1', BYTE * 2),
    ('wLEDWidth', WORD),
    ('wLEDHeight', WORD),
    ('byRes2', BYTE * 64),
])

NET_DVR_LED_SCREEN_CFG = struct_tagNET_DVR_LED_SCREEN_CFG
LPNET_DVR_LED_SCREEN_CFG = POINTER(struct_tagNET_DVR_LED_SCREEN_CFG)
tagNET_DVR_LED_SCREEN_CFG = struct_tagNET_DVR_LED_SCREEN_CFG
