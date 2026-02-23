from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PLAN_TEMPLATE_COND(Structure):
    pass

_S(struct_tagNET_DVR_PLAN_TEMPLATE_COND, [
    ('dwSize', DWORD),
    ('dwPlanTemplateNumber', DWORD),
    ('wLocalControllerID', WORD),
    ('byRes', BYTE * 106),
])

NET_DVR_PLAN_TEMPLATE_COND = struct_tagNET_DVR_PLAN_TEMPLATE_COND
LPNET_DVR_PLAN_TEMPLATE_COND = POINTER(struct_tagNET_DVR_PLAN_TEMPLATE_COND)
tagNET_DVR_PLAN_TEMPLATE_COND = struct_tagNET_DVR_PLAN_TEMPLATE_COND
