from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_one_output_schedule_rule import NET_DVR_ONE_OUTPUT_SCHEDULE_RULE


class struct_tagNET_DVR_OUTPUT_SCHEDULE_RULECFG(Structure):
    pass

_S(struct_tagNET_DVR_OUTPUT_SCHEDULE_RULECFG, [
    ('dwSize', DWORD),
    ('struOutputRule', NET_DVR_ONE_OUTPUT_SCHEDULE_RULE * 8),
    ('byRes', BYTE * 64),
])

NET_DVR_OUTPUT_SCHEDULE_RULECFG = struct_tagNET_DVR_OUTPUT_SCHEDULE_RULECFG
LPNET_DVR_OUTPUT_SCHEDULE_RULECFG = POINTER(struct_tagNET_DVR_OUTPUT_SCHEDULE_RULECFG)
tagNET_DVR_OUTPUT_SCHEDULE_RULECFG = struct_tagNET_DVR_OUTPUT_SCHEDULE_RULECFG
