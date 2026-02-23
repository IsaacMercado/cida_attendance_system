from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_schedule_choice import NET_DVR_SCHEDULE_CHOICE
from .net_dvr_time_v30 import NET_DVR_TIME_V30


class struct_tagNET_DVR_SCHEDULE_PLAN(Structure):
    pass

_S(struct_tagNET_DVR_SCHEDULE_PLAN, [
    ('dwSize', DWORD),
    ('bySchedulePlanNo', BYTE),
    ('bySchedulePlanType', BYTE),
    ('byEnable', BYTE),
    ('byRes1', BYTE),
    ('struScheduleChoice', NET_DVR_SCHEDULE_CHOICE * 7),
    ('struStartTime', NET_DVR_TIME_V30),
    ('struEndTime', NET_DVR_TIME_V30),
    ('byHolidayNo', BYTE),
    ('byRes', BYTE * 63),
])

NET_DVR_SCHEDULE_PLAN = struct_tagNET_DVR_SCHEDULE_PLAN
LPNET_DVR_SCHEDULE_PLAN = POINTER(struct_tagNET_DVR_SCHEDULE_PLAN)
tagNET_DVR_SCHEDULE_PLAN = struct_tagNET_DVR_SCHEDULE_PLAN
