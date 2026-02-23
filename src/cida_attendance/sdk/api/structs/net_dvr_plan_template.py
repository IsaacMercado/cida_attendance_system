from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PLAN_TEMPLATE(Structure):
    pass

_S(struct_tagNET_DVR_PLAN_TEMPLATE, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byRes1', BYTE * 3),
    ('byTemplateName', BYTE * 32),
    ('dwWeekPlanNo', DWORD),
    ('dwHolidayGroupNo', DWORD * 16),
    ('byRes2', BYTE * 32),
])

NET_DVR_PLAN_TEMPLATE = struct_tagNET_DVR_PLAN_TEMPLATE
LPNET_DVR_PLAN_TEMPLATE = POINTER(struct_tagNET_DVR_PLAN_TEMPLATE)
tagNET_DVR_PLAN_TEMPLATE = struct_tagNET_DVR_PLAN_TEMPLATE
