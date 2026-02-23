from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_schedule_plan import NET_DVR_SCHEDULE_PLAN


class struct_tagNET_DVR_SCHEDULE_INFO_CFG(Structure):
    pass

_S(struct_tagNET_DVR_SCHEDULE_INFO_CFG, [
    ('dwSize', DWORD),
    ('dwEmployeeNo', DWORD),
    ('byName', BYTE * 32),
    ('byDepartmentName', BYTE * 32),
    ('struSchedulePlan', NET_DVR_SCHEDULE_PLAN),
    ('byRes', BYTE * 128),
])

NET_DVR_SCHEDULE_INFO_CFG = struct_tagNET_DVR_SCHEDULE_INFO_CFG
LPNET_DVR_SCHEDULE_INFO_CFG = POINTER(struct_tagNET_DVR_SCHEDULE_INFO_CFG)
tagNET_DVR_SCHEDULE_INFO_CFG = struct_tagNET_DVR_SCHEDULE_INFO_CFG
