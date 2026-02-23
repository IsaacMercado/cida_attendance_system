from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_its_overlap_info_param import NET_ITS_OVERLAP_INFO_PARAM
from .net_its_overlap_item_param import NET_ITS_OVERLAP_ITEM_PARAM


class struct_tagNET_ITS_OVERLAP_CFG(Structure):
    pass

_S(struct_tagNET_ITS_OVERLAP_CFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byRes1', BYTE * 3),
    ('struOverLapItem', NET_ITS_OVERLAP_ITEM_PARAM),
    ('struOverLapInfo', NET_ITS_OVERLAP_INFO_PARAM),
    ('byRes', BYTE * 32),
])

NET_ITS_OVERLAP_CFG = struct_tagNET_ITS_OVERLAP_CFG
LPNET_ITS_OVERLAP_CFG = POINTER(struct_tagNET_ITS_OVERLAP_CFG)
tagNET_ITS_OVERLAP_CFG = struct_tagNET_ITS_OVERLAP_CFG
