from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_one_tps_rule import NET_DVR_ONE_TPS_RULE


class struct_tagNET_DVR_TPS_RULECFG(Structure):
    pass

_S(struct_tagNET_DVR_TPS_RULECFG, [
    ('dwSize', DWORD),
    ('struOneTpsRule', NET_DVR_ONE_TPS_RULE * 8),
    ('byRes2', BYTE * 40),
])

NET_DVR_TPS_RULECFG = struct_tagNET_DVR_TPS_RULECFG
LPNET_DVR_TPS_RULECFG = POINTER(struct_tagNET_DVR_TPS_RULECFG)
tagNET_DVR_TPS_RULECFG = struct_tagNET_DVR_TPS_RULECFG
