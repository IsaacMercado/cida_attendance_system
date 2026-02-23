from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SCREEN_CONFIG(Structure):
    pass

_S(struct_tagNET_DVR_SCREEN_CONFIG, [
    ('dwSize', DWORD),
    ('byVolume', BYTE),
    ('byContrast', BYTE),
    ('byBrightness', BYTE),
    ('byScreenShowEnabled', BYTE),
    ('byScreenLocked', BYTE),
    ('byBlackScreenEnabled', BYTE),
    ('byRes', BYTE * 30),
])

NET_DVR_SCREEN_CONFIG = struct_tagNET_DVR_SCREEN_CONFIG
LPNET_DVR_SCREEN_CONFIG = POINTER(struct_tagNET_DVR_SCREEN_CONFIG)
tagNET_DVR_SCREEN_CONFIG = struct_tagNET_DVR_SCREEN_CONFIG
