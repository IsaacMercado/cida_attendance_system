from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_single_plan_segment import NET_DVR_SINGLE_PLAN_SEGMENT


class struct_tagNET_DVR_WEEK_PLAN_CFG(Structure):
    pass

_S(struct_tagNET_DVR_WEEK_PLAN_CFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byRes1', BYTE * 3),
    ('struPlanCfg', (NET_DVR_SINGLE_PLAN_SEGMENT * 8) * 7),
    ('byRes2', BYTE * 16),
])

NET_DVR_WEEK_PLAN_CFG = struct_tagNET_DVR_WEEK_PLAN_CFG
LPNET_DVR_WEEK_PLAN_CFG = POINTER(struct_tagNET_DVR_WEEK_PLAN_CFG)
tagNET_DVR_WEEK_PLAN_CFG = struct_tagNET_DVR_WEEK_PLAN_CFG
