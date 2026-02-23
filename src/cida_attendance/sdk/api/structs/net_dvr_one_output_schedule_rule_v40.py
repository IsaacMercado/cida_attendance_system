from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_output_schedule import NET_DVR_OUTPUT_SCHEDULE
from .net_dvr_scheddate import NET_DVR_SCHEDDATE


class struct_tagNET_DVR_ONE_OUTPUT_SCHEDULE_RULE_V40(Structure):
    pass

_S(struct_tagNET_DVR_ONE_OUTPUT_SCHEDULE_RULE_V40, [
    ('byEnable', BYTE),
    ('byRes1', BYTE * 3),
    ('struDate', NET_DVR_SCHEDDATE),
    ('struOutputSchedule', NET_DVR_OUTPUT_SCHEDULE * 8),
    ('byTriggerIndex', BYTE * 512),
    ('byRes2', BYTE * 64),
])

NET_DVR_ONE_OUTPUT_SCHEDULE_RULE_V40 = struct_tagNET_DVR_ONE_OUTPUT_SCHEDULE_RULE_V40
LPNET_DVR_ONE_OUTPUT_SCHEDULE_RULE_V40 = POINTER(struct_tagNET_DVR_ONE_OUTPUT_SCHEDULE_RULE_V40)
tagNET_DVR_ONE_OUTPUT_SCHEDULE_RULE_V40 = struct_tagNET_DVR_ONE_OUTPUT_SCHEDULE_RULE_V40
