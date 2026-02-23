from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_plan_item import NET_DVR_PLAN_ITEM


class struct_tagNET_DVR_PLAYPLAN_CFG(Structure):
    pass

_S(struct_tagNET_DVR_PLAYPLAN_CFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byPlanMode', BYTE),
    ('byRes', BYTE * 2),
    ('struPlanItem', (NET_DVR_PLAN_ITEM * 8) * 7),
    ('dwPlayPlanNo', DWORD),
    ('byPlayPlanName', BYTE * 32),
    ('byRes2', BYTE * 32),
])

NET_DVR_PLAYPLAN_CFG = struct_tagNET_DVR_PLAYPLAN_CFG
LPNET_DVR_PLAYPLAN_CFG = POINTER(struct_tagNET_DVR_PLAYPLAN_CFG)
tagNET_DVR_PLAYPLAN_CFG = struct_tagNET_DVR_PLAYPLAN_CFG
