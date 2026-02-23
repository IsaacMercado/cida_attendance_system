from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_screen_vga_cfg import NET_DVR_SCREEN_VGA_CFG


class struct_tagNET_DVR_LED_INPUT_CFG(Structure):
    pass

_S(struct_tagNET_DVR_LED_INPUT_CFG, [
    ('dwSize', DWORD),
    ('dwResolutionWidth', DWORD),
    ('dwResolutionHeight', DWORD),
    ('dwRefreshRate', DWORD),
    ('struVgaCfg', NET_DVR_SCREEN_VGA_CFG),
    ('byRes', BYTE * 32),
])

NET_DVR_LED_INPUT_CFG = struct_tagNET_DVR_LED_INPUT_CFG
LPNET_DVR_LED_INPUT_CFG = POINTER(struct_tagNET_DVR_LED_INPUT_CFG)
tagNET_DVR_LED_INPUT_CFG = struct_tagNET_DVR_LED_INPUT_CFG
