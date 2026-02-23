from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_LED_OUTPUT_CFG(Structure):
    pass

_S(struct_tagNET_DVR_LED_OUTPUT_CFG, [
    ('dwSize', DWORD),
    ('byEnableZoom', BYTE),
    ('byAutoCutBlackEdge', BYTE),
    ('byRes1', BYTE * 2),
    ('wLEDWidth', WORD),
    ('wLEDHeight', WORD),
    ('dwRefreshRate', DWORD),
    ('dwInputNO', DWORD),
    ('byRes2', BYTE * 32),
])

NET_DVR_LED_OUTPUT_CFG = struct_tagNET_DVR_LED_OUTPUT_CFG
LPNET_DVR_LED_OUTPUT_CFG = POINTER(struct_tagNET_DVR_LED_OUTPUT_CFG)
tagNET_DVR_LED_OUTPUT_CFG = struct_tagNET_DVR_LED_OUTPUT_CFG
