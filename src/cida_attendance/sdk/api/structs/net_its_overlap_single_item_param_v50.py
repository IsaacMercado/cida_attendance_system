from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_ITS_OVERLAP_SINGLE_ITEM_PARAM_V50(Structure):
    pass

_S(struct_tagNET_ITS_OVERLAP_SINGLE_ITEM_PARAM_V50, [
    ('byRes1', BYTE * 2),
    ('byItemType', BYTE),
    ('byChangeLineNum', BYTE),
    ('bySpaceNum', BYTE),
    ('byRes2', BYTE * 2),
    ('byEnablePos', BYTE),
    ('wStartPosTop', WORD),
    ('wStartPosLeft', WORD),
    ('byItemTypeCustom', BYTE * 32),
    ('byRes', BYTE * 8),
])

NET_ITS_OVERLAP_SINGLE_ITEM_PARAM_V50 = struct_tagNET_ITS_OVERLAP_SINGLE_ITEM_PARAM_V50
LPNET_ITS_OVERLAP_SINGLE_ITEM_PARAM_V50 = POINTER(struct_tagNET_ITS_OVERLAP_SINGLE_ITEM_PARAM_V50)
tagNET_ITS_OVERLAP_SINGLE_ITEM_PARAM_V50 = struct_tagNET_ITS_OVERLAP_SINGLE_ITEM_PARAM_V50
