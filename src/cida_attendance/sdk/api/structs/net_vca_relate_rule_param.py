from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_VCA_RELATE_RULE_PARAM(Structure):
    pass

_S(struct_tagNET_VCA_RELATE_RULE_PARAM, [
    ('byRuleID', BYTE),
    ('byRes', BYTE),
    ('wEventType', WORD),
])

NET_VCA_RELATE_RULE_PARAM = struct_tagNET_VCA_RELATE_RULE_PARAM
LPNET_VCA_RELATE_RULE_PARAM = POINTER(struct_tagNET_VCA_RELATE_RULE_PARAM)
tagNET_VCA_RELATE_RULE_PARAM = struct_tagNET_VCA_RELATE_RULE_PARAM
