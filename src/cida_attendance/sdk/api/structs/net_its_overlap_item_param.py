from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_its_overlap_single_item_param import NET_ITS_OVERLAP_SINGLE_ITEM_PARAM


class struct_tagNET_ITS_OVERLAP_ITEM_PARAM(Structure):
    pass

_S(struct_tagNET_ITS_OVERLAP_ITEM_PARAM, [
    ('struSingleItem', NET_ITS_OVERLAP_SINGLE_ITEM_PARAM * 50),
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
    ('byRes', BYTE * 23),
])

NET_ITS_OVERLAP_ITEM_PARAM = struct_tagNET_ITS_OVERLAP_ITEM_PARAM
LPNET_ITS_OVERLAP_ITEM_PARAM = POINTER(struct_tagNET_ITS_OVERLAP_ITEM_PARAM)
tagNET_ITS_OVERLAP_ITEM_PARAM = struct_tagNET_ITS_OVERLAP_ITEM_PARAM
