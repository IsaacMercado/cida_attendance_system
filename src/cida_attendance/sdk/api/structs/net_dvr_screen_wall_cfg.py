from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SCREEN_WALL_CFG(Structure):
    pass

_S(struct_tagNET_DVR_SCREEN_WALL_CFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byRes', BYTE * 35),
])

NET_DVR_SCREEN_WALL_CFG = struct_tagNET_DVR_SCREEN_WALL_CFG
LPNET_DVR_SCREEN_WALL_CFG = POINTER(struct_tagNET_DVR_SCREEN_WALL_CFG)
tagNET_DVR_SCREEN_WALL_CFG = struct_tagNET_DVR_SCREEN_WALL_CFG
