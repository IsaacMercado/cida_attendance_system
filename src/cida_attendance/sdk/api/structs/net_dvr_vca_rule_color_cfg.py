from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_pic_info import NET_DVR_PIC_INFO


class struct_tagNET_DVR_VCA_RULE_COLOR_CFG(Structure):
    pass

_S(struct_tagNET_DVR_VCA_RULE_COLOR_CFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byRuleID', BYTE),
    ('byColorBlockNo', BYTE),
    ('byRes1', BYTE),
    ('struPicInfo', NET_DVR_PIC_INFO),
    ('byRes', BYTE * 64),
])

NET_DVR_VCA_RULE_COLOR_CFG = struct_tagNET_DVR_VCA_RULE_COLOR_CFG
LPNET_DVR_VCA_RULE_COLOR_CFG = POINTER(struct_tagNET_DVR_VCA_RULE_COLOR_CFG)
tagNET_DVR_VCA_RULE_COLOR_CFG = struct_tagNET_DVR_VCA_RULE_COLOR_CFG
