from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SCREEN_WALL_CTRL(Structure):
    pass

_S(struct_tagNET_DVR_SCREEN_WALL_CTRL, [
    ('byEnable', BYTE),
    ('byRes', BYTE * 15),
])

NET_DVR_SCREEN_WALL_CTRL = struct_tagNET_DVR_SCREEN_WALL_CTRL
LPNET_DVR_SCREEN_WALL_CTRL = POINTER(struct_tagNET_DVR_SCREEN_WALL_CTRL)
tagNET_DVR_SCREEN_WALL_CTRL = struct_tagNET_DVR_SCREEN_WALL_CTRL
