from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_WEEK_PLAN_COND(Structure):
    pass

_S(struct_tagNET_DVR_WEEK_PLAN_COND, [
    ('dwSize', DWORD),
    ('dwWeekPlanNumber', DWORD),
    ('wLocalControllerID', WORD),
    ('byRes', BYTE * 106),
])

NET_DVR_WEEK_PLAN_COND = struct_tagNET_DVR_WEEK_PLAN_COND
LPNET_DVR_WEEK_PLAN_COND = POINTER(struct_tagNET_DVR_WEEK_PLAN_COND)
tagNET_DVR_WEEK_PLAN_COND = struct_tagNET_DVR_WEEK_PLAN_COND
