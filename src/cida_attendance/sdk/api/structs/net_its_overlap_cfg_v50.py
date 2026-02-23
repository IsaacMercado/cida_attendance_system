from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_its_overlap_info_param import NET_ITS_OVERLAP_INFO_PARAM
from .net_its_overlap_item_param_v50 import NET_ITS_OVERLAP_ITEM_PARAM_V50


class struct_tagNET_ITS_OVERLAP_CFG_V50(Structure):
    pass

_S(struct_tagNET_ITS_OVERLAP_CFG_V50, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byRes1', BYTE * 3),
    ('struOverLapItemV50', NET_ITS_OVERLAP_ITEM_PARAM_V50),
    ('struOverLapInfo', NET_ITS_OVERLAP_INFO_PARAM),
    ('byRes', BYTE * 120),
])

NET_ITS_OVERLAP_CFG_V50 = struct_tagNET_ITS_OVERLAP_CFG_V50
LPNET_ITS_OVERLAP_CFG_V50 = POINTER(struct_tagNET_ITS_OVERLAP_CFG_V50)
tagNET_ITS_OVERLAP_CFG_V50 = struct_tagNET_ITS_OVERLAP_CFG_V50
