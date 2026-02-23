from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVRSCREEN_SPLICE_CFG(Structure):
    pass

_S(struct_tagNET_DVRSCREEN_SPLICE_CFG, [
    ('dwSize', DWORD),
    ('bySpliceIndex', BYTE),
    ('bySpliceX', BYTE),
    ('bySpliceY', BYTE),
    ('byWidth', BYTE),
    ('byHeight', BYTE),
    ('byRes', BYTE * 11),
])

NET_DVR_SCREEN_SPLICE_CFG = struct_tagNET_DVRSCREEN_SPLICE_CFG
LPNET_DVR_SCREEN_SPLICE_CFG = POINTER(struct_tagNET_DVRSCREEN_SPLICE_CFG)
tagNET_DVRSCREEN_SPLICE_CFG = struct_tagNET_DVRSCREEN_SPLICE_CFG
