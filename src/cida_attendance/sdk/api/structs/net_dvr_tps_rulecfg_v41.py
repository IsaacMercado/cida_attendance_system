from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_one_tps_rule_v41 import NET_DVR_ONE_TPS_RULE_V41


class struct_tagNET_DVR_TPS_RULECFG_V41(Structure):
    pass

_S(struct_tagNET_DVR_TPS_RULECFG_V41, [
    ('dwSize', DWORD),
    ('struOneTpsRule', NET_DVR_ONE_TPS_RULE_V41 * 8),
    ('byRes', BYTE * 128),
])

NET_DVR_TPS_RULECFG_V41 = struct_tagNET_DVR_TPS_RULECFG_V41
LPNET_DVR_TPS_RULECFG_V41 = POINTER(struct_tagNET_DVR_TPS_RULECFG_V41)
tagNET_DVR_TPS_RULECFG_V41 = struct_tagNET_DVR_TPS_RULECFG_V41
