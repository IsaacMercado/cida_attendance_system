from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_multi_card_group_cfg_v50 import NET_DVR_MULTI_CARD_GROUP_CFG_V50


class struct_tagNET_DVR_MULTI_CARD_CFG_V50(Structure):
    pass

_S(struct_tagNET_DVR_MULTI_CARD_CFG_V50, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('bySwipeIntervalTimeout', BYTE),
    ('byRes1', BYTE * 2),
    ('struGroupCfg', NET_DVR_MULTI_CARD_GROUP_CFG_V50 * 20),
    ('byRes2', BYTE * 32),
])

NET_DVR_MULTI_CARD_CFG_V50 = struct_tagNET_DVR_MULTI_CARD_CFG_V50
LPNET_DVR_MULTI_CARD_CFG_V50 = POINTER(struct_tagNET_DVR_MULTI_CARD_CFG_V50)
tagNET_DVR_MULTI_CARD_CFG_V50 = struct_tagNET_DVR_MULTI_CARD_CFG_V50
