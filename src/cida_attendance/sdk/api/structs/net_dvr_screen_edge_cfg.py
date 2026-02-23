from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SCREEN_EDGE_CFG(Structure):
    pass

_S(struct_tagNET_DVR_SCREEN_EDGE_CFG, [
    ('byEnable', BYTE),
    ('byLeftEdge', BYTE),
    ('byRightEdge', BYTE),
    ('byTopEdge', BYTE),
    ('byLowerEdge', BYTE),
    ('byRes', BYTE * 7),
])

NET_DVR_SCREEN_EDGE_CFG = struct_tagNET_DVR_SCREEN_EDGE_CFG
LPNET_DVR_SCREEN_EDGE_CFG = POINTER(struct_tagNET_DVR_SCREEN_EDGE_CFG)
tagNET_DVR_SCREEN_EDGE_CFG = struct_tagNET_DVR_SCREEN_EDGE_CFG
