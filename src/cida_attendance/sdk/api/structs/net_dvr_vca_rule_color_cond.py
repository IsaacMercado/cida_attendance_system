from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_VCA_RULE_COLOR_COND(Structure):
    pass

_S(struct_tagNET_DVR_VCA_RULE_COLOR_COND, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('byRuleID', BYTE),
    ('byRes', BYTE * 127),
])

NET_DVR_VCA_RULE_COLOR_COND = struct_tagNET_DVR_VCA_RULE_COLOR_COND
LPNET_DVR_VCA_RULE_COLOR_COND = POINTER(struct_tagNET_DVR_VCA_RULE_COLOR_COND)
tagNET_DVR_VCA_RULE_COLOR_COND = struct_tagNET_DVR_VCA_RULE_COLOR_COND
