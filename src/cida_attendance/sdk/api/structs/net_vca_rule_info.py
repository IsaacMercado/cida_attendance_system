from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from ..enums import VCA_EVENT_TYPE
from .net_vca_event_union import NET_VCA_EVENT_UNION


class struct_tagNET_VCA_RULE_INFO(Structure):
    pass

_S(struct_tagNET_VCA_RULE_INFO, [
    ('byRuleID', BYTE),
    ('bySceneID', BYTE),
    ('wEventTypeEx', WORD),
    ('byRuleName', BYTE * 32),
    ('dwEventType', VCA_EVENT_TYPE),
    ('uEventParam', NET_VCA_EVENT_UNION),
])

NET_VCA_RULE_INFO = struct_tagNET_VCA_RULE_INFO
LPNET_VCA_RULE_INFO = POINTER(struct_tagNET_VCA_RULE_INFO)
tagNET_VCA_RULE_INFO = struct_tagNET_VCA_RULE_INFO
