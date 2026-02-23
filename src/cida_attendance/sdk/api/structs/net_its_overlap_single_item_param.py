from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_ITS_OVERLAP_SINGLE_ITEM_PARAM(Structure):
    pass

_S(struct_tagNET_ITS_OVERLAP_SINGLE_ITEM_PARAM, [
    ('byRes1', BYTE * 2),
    ('byItemType', BYTE),
    ('byChangeLineNum', BYTE),
    ('bySpaceNum', BYTE),
    ('byRes2', BYTE * 2),
    ('byEnablePos', BYTE),
    ('wStartPosTop', WORD),
    ('wStartPosLeft', WORD),
    ('byRes', BYTE * 8),
])

NET_ITS_OVERLAP_SINGLE_ITEM_PARAM = struct_tagNET_ITS_OVERLAP_SINGLE_ITEM_PARAM
LPNET_ITS_OVERLAP_SINGLE_ITEM_PARAM = POINTER(struct_tagNET_ITS_OVERLAP_SINGLE_ITEM_PARAM)
tagNET_ITS_OVERLAP_SINGLE_ITEM_PARAM = struct_tagNET_ITS_OVERLAP_SINGLE_ITEM_PARAM
