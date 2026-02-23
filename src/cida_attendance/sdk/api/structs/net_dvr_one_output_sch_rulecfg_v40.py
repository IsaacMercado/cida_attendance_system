from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_one_output_schedule_rule_v40 import NET_DVR_ONE_OUTPUT_SCHEDULE_RULE_V40


class struct_tagNET_DVR_ONE_OUTPUT_SCH_RULECFG_V40(Structure):
    pass

_S(struct_tagNET_DVR_ONE_OUTPUT_SCH_RULECFG_V40, [
    ('dwSize', DWORD),
    ('struOutputRule', NET_DVR_ONE_OUTPUT_SCHEDULE_RULE_V40),
    ('byRes', BYTE * 256),
])

NET_DVR_ONE_OUTPUT_SCH_RULECFG_V40 = struct_tagNET_DVR_ONE_OUTPUT_SCH_RULECFG_V40
LPNET_DVR_ONE_OUTPUT_SCH_RULECFG_V40 = POINTER(struct_tagNET_DVR_ONE_OUTPUT_SCH_RULECFG_V40)
tagNET_DVR_ONE_OUTPUT_SCH_RULECFG_V40 = struct_tagNET_DVR_ONE_OUTPUT_SCH_RULECFG_V40
