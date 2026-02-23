from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_its_overlap_single_item_param_v50 import NET_ITS_OVERLAP_SINGLE_ITEM_PARAM_V50


class struct_tagNET_ITS_OVERLAP_ITEM_PARAM_V50(Structure):
    pass

_S(struct_tagNET_ITS_OVERLAP_ITEM_PARAM_V50, [
    ('struSingleItem', NET_ITS_OVERLAP_SINGLE_ITEM_PARAM_V50 * 50),
    ('dwLinePercent', DWORD),
    ('dwItemsStlye', DWORD),
    ('wStartPosTop', WORD),
    ('wStartPosLeft', WORD),
    ('wCharStyle', WORD),
    ('wCharSize', WORD),
    ('wCharInterval', WORD),
    ('byRes1', BYTE * 2),
    ('dwForeClorRGB', DWORD),
    ('dwBackClorRGB', DWORD),
    ('byColorAdapt', BYTE),
    ('byParamFillZeroEnble', BYTE),
    ('byPlateLeftCornerEnable', BYTE),
    ('byRes2', BYTE),
    ('wStartSPicPosTop', WORD),
    ('wStartSPicPosLeft', WORD),
    ('byOsdLocate', BYTE),
    ('byRes', BYTE * 63),
])

NET_ITS_OVERLAP_ITEM_PARAM_V50 = struct_tagNET_ITS_OVERLAP_ITEM_PARAM_V50
LPNET_ITS_OVERLAP_ITEM_PARAM_V50 = POINTER(struct_tagNET_ITS_OVERLAP_ITEM_PARAM_V50)
tagNET_ITS_OVERLAP_ITEM_PARAM_V50 = struct_tagNET_ITS_OVERLAP_ITEM_PARAM_V50
