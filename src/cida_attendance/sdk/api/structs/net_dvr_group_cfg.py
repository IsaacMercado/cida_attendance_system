from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_valid_period_cfg import NET_DVR_VALID_PERIOD_CFG


class struct__tagNET_DVR_GROUP_CFG(Structure):
    pass

_S(struct__tagNET_DVR_GROUP_CFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byRes1', BYTE * 3),
    ('struValidPeriodCfg', NET_DVR_VALID_PERIOD_CFG),
    ('byGroupName', BYTE * 32),
    ('byRes2', BYTE * 32),
])

NET_DVR_GROUP_CFG = struct__tagNET_DVR_GROUP_CFG
LPNET_DVR_GROUP_CFG = POINTER(struct__tagNET_DVR_GROUP_CFG)
_tagNET_DVR_GROUP_CFG = struct__tagNET_DVR_GROUP_CFG
