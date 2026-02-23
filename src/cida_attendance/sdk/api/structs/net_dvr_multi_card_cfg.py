from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_multi_card_group_cfg import NET_DVR_MULTI_CARD_GROUP_CFG


class struct_tagNET_DVR_MULTI_CARD_CFG(Structure):
    pass

_S(struct_tagNET_DVR_MULTI_CARD_CFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('bySwipeIntervalTimeout', BYTE),
    ('byRes1', BYTE * 2),
    ('struGroupCfg', NET_DVR_MULTI_CARD_GROUP_CFG * 4),
    ('byRes2', BYTE * 32),
])

NET_DVR_MULTI_CARD_CFG = struct_tagNET_DVR_MULTI_CARD_CFG
LPNET_DVR_MULTI_CARD_CFG = POINTER(struct_tagNET_DVR_MULTI_CARD_CFG)
tagNET_DVR_MULTI_CARD_CFG = struct_tagNET_DVR_MULTI_CARD_CFG
