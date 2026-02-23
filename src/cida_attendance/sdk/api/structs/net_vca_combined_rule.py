from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_relate_rule_param import NET_VCA_RELATE_RULE_PARAM


class struct_tagNET_VCA_COMBINED_RULE_(Structure):
    pass

_S(struct_tagNET_VCA_COMBINED_RULE_, [
    ('byRuleSequence', BYTE),
    ('byRes', BYTE * 7),
    ('dwMinInterval', DWORD),
    ('dwMaxInterval', DWORD),
    ('struRule1Raram', NET_VCA_RELATE_RULE_PARAM),
    ('struRule2Raram', NET_VCA_RELATE_RULE_PARAM),
    ('byRes1', BYTE * 36),
])

NET_VCA_COMBINED_RULE = struct_tagNET_VCA_COMBINED_RULE_
LPNET_VCA_COMBINED_RULE = POINTER(struct_tagNET_VCA_COMBINED_RULE_)
tagNET_VCA_COMBINED_RULE_ = struct_tagNET_VCA_COMBINED_RULE_
