from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_cycle_time import NET_DVR_CYCLE_TIME
from .net_dvr_plan_info import NET_DVR_PLAN_INFO
from .net_dvr_time_ex import NET_DVR_TIME_EX


class struct_tagNET_DVR_PLAN_CFG(Structure):
    pass

_S(struct_tagNET_DVR_PLAN_CFG, [
    ('dwSize', DWORD),
    ('byValid', BYTE),
    ('byWorkMode', BYTE),
    ('byWallNo', BYTE),
    ('byPlanNo', BYTE),
    ('byPlanName', BYTE * 32),
    ('struTime', NET_DVR_TIME_EX),
    ('struTimeCycle', NET_DVR_CYCLE_TIME * 7),
    ('dwWorkCount', DWORD),
    ('strPlanEntry', NET_DVR_PLAN_INFO * 32),
    ('dwPlanNo', DWORD),
    ('byRes2', BYTE * 60),
])

NET_DVR_PLAN_CFG = struct_tagNET_DVR_PLAN_CFG
LPNET_DVR_PLAN_CFG = POINTER(struct_tagNET_DVR_PLAN_CFG)
tagNET_DVR_PLAN_CFG = struct_tagNET_DVR_PLAN_CFG
