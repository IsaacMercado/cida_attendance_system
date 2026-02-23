from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_group_combination_info_v50 import NET_DVR_GROUP_COMBINATION_INFO_V50


class struct_tagNET_DVR_MULTI_CARD_GROUP_CFG_V50(Structure):
    pass

_S(struct_tagNET_DVR_MULTI_CARD_GROUP_CFG_V50, [
    ('byEnable', BYTE),
    ('byEnableOfflineVerifyMode', BYTE),
    ('byRes1', BYTE * 2),
    ('dwTemplateNo', DWORD),
    ('struGroupCombination', NET_DVR_GROUP_COMBINATION_INFO_V50 * 8),
])

NET_DVR_MULTI_CARD_GROUP_CFG_V50 = struct_tagNET_DVR_MULTI_CARD_GROUP_CFG_V50
LPNET_DVR_MULTI_CARD_GROUP_CFG_V50 = POINTER(struct_tagNET_DVR_MULTI_CARD_GROUP_CFG_V50)
tagNET_DVR_MULTI_CARD_GROUP_CFG_V50 = struct_tagNET_DVR_MULTI_CARD_GROUP_CFG_V50
