from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_ptz_position import NET_DVR_PTZ_POSITION
from .net_vca_rulecfg import NET_VCA_RULECFG


class struct_tagNET_DVR_POSITION_RULE_CFG(Structure):
    pass

_S(struct_tagNET_DVR_POSITION_RULE_CFG, [
    ('dwSize', DWORD),
    ('struPtzPosition', NET_DVR_PTZ_POSITION),
    ('struVcaRuleCfg', NET_VCA_RULECFG),
    ('byRes2', BYTE * 80),
])

NET_DVR_POSITION_RULE_CFG = struct_tagNET_DVR_POSITION_RULE_CFG
LPNET_DVR_POSITION_RULE_CFG = POINTER(struct_tagNET_DVR_POSITION_RULE_CFG)
tagNET_DVR_POSITION_RULE_CFG = struct_tagNET_DVR_POSITION_RULE_CFG
