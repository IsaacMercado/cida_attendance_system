from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SCREEN_MENU_CFG(Structure):
    pass

_S(struct_tagNET_DVR_SCREEN_MENU_CFG, [
    ('dwSize', DWORD),
    ('byMenuLanguage', BYTE),
    ('byTransparency', BYTE),
    ('byDuration', BYTE),
    ('byRes', BYTE * 13),
])

NET_DVR_SCREEN_MENU_CFG = struct_tagNET_DVR_SCREEN_MENU_CFG
LPNET_DVR_SCREEN_MENU_CFG = POINTER(struct_tagNET_DVR_SCREEN_MENU_CFG)
tagNET_DVR_SCREEN_MENU_CFG = struct_tagNET_DVR_SCREEN_MENU_CFG
