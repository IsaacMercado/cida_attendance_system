from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_date import NET_DVR_DATE
from .net_dvr_single_plan_segment import NET_DVR_SINGLE_PLAN_SEGMENT


class struct_tagNET_DVR_HOLIDAY_PLAN_CFG(Structure):
    pass

_S(struct_tagNET_DVR_HOLIDAY_PLAN_CFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byRes1', BYTE * 3),
    ('struBeginDate', NET_DVR_DATE),
    ('struEndDate', NET_DVR_DATE),
    ('struPlanCfg', NET_DVR_SINGLE_PLAN_SEGMENT * 8),
    ('byRes2', BYTE * 16),
])

NET_DVR_HOLIDAY_PLAN_CFG = struct_tagNET_DVR_HOLIDAY_PLAN_CFG
LPNET_DVR_HOLIDAY_PLAN_CFG = POINTER(struct_tagNET_DVR_HOLIDAY_PLAN_CFG)
tagNET_DVR_HOLIDAY_PLAN_CFG = struct_tagNET_DVR_HOLIDAY_PLAN_CFG
