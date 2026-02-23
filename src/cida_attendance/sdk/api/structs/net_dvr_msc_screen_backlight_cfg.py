from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_MSC_SCREEN_BACKLIGHT_CFG(Structure):
    pass

_S(struct_tagNET_DVR_MSC_SCREEN_BACKLIGHT_CFG, [
    ('dwSize', DWORD),
    ('byBacklight', BYTE),
    ('byRes', BYTE * 15),
])

NET_DVR_MSC_SCREEN_BACKLIGHT_CFG = struct_tagNET_DVR_MSC_SCREEN_BACKLIGHT_CFG
LPNET_DVR_MSC_SCREEN_BACKLIGHT_CFG = POINTER(struct_tagNET_DVR_MSC_SCREEN_BACKLIGHT_CFG)
tagNET_DVR_MSC_SCREEN_BACKLIGHT_CFG = struct_tagNET_DVR_MSC_SCREEN_BACKLIGHT_CFG
