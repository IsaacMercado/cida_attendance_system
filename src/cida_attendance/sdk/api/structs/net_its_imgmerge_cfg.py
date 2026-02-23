from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_ITS_IMGMERGE_CFG(Structure):
    pass

_S(struct_tagNET_ITS_IMGMERGE_CFG, [
    ('dwSize', DWORD),
    ('byIsMerge', BYTE),
    ('byCloseupProportion', BYTE),
    ('byRes1', BYTE * 2),
    ('dwOneMergeType', DWORD),
    ('dwTwoMergeType', DWORD),
    ('dwThreeMergeType', DWORD),
    ('dwJpegQuality', DWORD),
    ('dwCloseupIndex', DWORD),
    ('dwMerageMaxSize', DWORD),
    ('wCloseupDeviation', WORD),
    ('byRes', BYTE * 30),
])

NET_ITS_IMGMERGE_CFG = struct_tagNET_ITS_IMGMERGE_CFG
LPNET_ITS_IMGMERGE_CFG = POINTER(struct_tagNET_ITS_IMGMERGE_CFG)
tagNET_ITS_IMGMERGE_CFG = struct_tagNET_ITS_IMGMERGE_CFG
