from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_WALL_RELATION_CFG(Structure):
    pass

_S(struct_tagNET_DVR_WALL_RELATION_CFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byRealWallNo', BYTE),
    ('byRes', BYTE * 14),
])

NET_DVR_WALL_RELATION_CFG = struct_tagNET_DVR_WALL_RELATION_CFG
LPNET_DVR_WALL_RELATION_CFG = POINTER(struct_tagNET_DVR_WALL_RELATION_CFG)
tagNET_DVR_WALL_RELATION_CFG = struct_tagNET_DVR_WALL_RELATION_CFG
