from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_ptz_position import NET_DVR_PTZ_POSITION
from .net_vca_rulecfg_v41 import NET_VCA_RULECFG_V41


class struct_tagNET_DVR_POSITION_RULE_CFG_V41(Structure):
    pass

_S(struct_tagNET_DVR_POSITION_RULE_CFG_V41, [
    ('dwSize', DWORD),
    ('struPtzPosition', NET_DVR_PTZ_POSITION),
    ('struVcaRuleCfg', NET_VCA_RULECFG_V41),
    ('byTrackEnable', BYTE),
    ('byRes1', BYTE),
    ('wTrackDuration', WORD),
    ('byRes2', BYTE * 76),
])

NET_DVR_POSITION_RULE_CFG_V41 = struct_tagNET_DVR_POSITION_RULE_CFG_V41
LPNET_DVR_POSITION_RULE_CFG_V41 = POINTER(struct_tagNET_DVR_POSITION_RULE_CFG_V41)
tagNET_DVR_POSITION_RULE_CFG_V41 = struct_tagNET_DVR_POSITION_RULE_CFG_V41
