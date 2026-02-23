from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_group_combination_info import NET_DVR_GROUP_COMBINATION_INFO


class struct_tagNET_DVR_MULTI_CARD_GROUP_CFG(Structure):
    pass

_S(struct_tagNET_DVR_MULTI_CARD_GROUP_CFG, [
    ('byEnable', BYTE),
    ('byEnableOfflineVerifyMode', BYTE),
    ('byRes1', BYTE * 2),
    ('dwTemplateNo', DWORD),
    ('struGroupCombination', NET_DVR_GROUP_COMBINATION_INFO * 8),
])

NET_DVR_MULTI_CARD_GROUP_CFG = struct_tagNET_DVR_MULTI_CARD_GROUP_CFG
LPNET_DVR_MULTI_CARD_GROUP_CFG = POINTER(struct_tagNET_DVR_MULTI_CARD_GROUP_CFG)
tagNET_DVR_MULTI_CARD_GROUP_CFG = struct_tagNET_DVR_MULTI_CARD_GROUP_CFG
