from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_output_schedule import NET_DVR_OUTPUT_SCHEDULE
from .net_dvr_scheddate import NET_DVR_SCHEDDATE


class struct_tagNET_DVR_ONE_OUTPUT_SCHEDULE_RULE(Structure):
    pass

_S(struct_tagNET_DVR_ONE_OUTPUT_SCHEDULE_RULE, [
    ('byEnable', BYTE),
    ('byRes1', BYTE * 3),
    ('struDate', NET_DVR_SCHEDDATE),
    ('struOutputSchedule', NET_DVR_OUTPUT_SCHEDULE * 8),
    ('byRes2', BYTE * 16),
])

NET_DVR_ONE_OUTPUT_SCHEDULE_RULE = struct_tagNET_DVR_ONE_OUTPUT_SCHEDULE_RULE
LPNET_DVR_ONE_OUTPUT_SCHEDULE_RULE = POINTER(struct_tagNET_DVR_ONE_OUTPUT_SCHEDULE_RULE)
tagNET_DVR_ONE_OUTPUT_SCHEDULE_RULE = struct_tagNET_DVR_ONE_OUTPUT_SCHEDULE_RULE
