from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from ..enums import VCA_EVENT_TYPE
from .anon_6 import NET_DVR_SCHEDTIME
from .anon_7 import NET_DVR_HANDLEEXCEPTION_V30
from .net_vca_event_union import NET_VCA_EVENT_UNION
from .net_vca_filter_strategy import NET_VCA_FILTER_STRATEGY
from .net_vca_rule_trigger_param import NET_VCA_RULE_TRIGGER_PARAM
from .net_vca_size_filter import NET_VCA_SIZE_FILTER


class struct_tagNET_VCA_ONE_RULE_V41(Structure):
    pass

_S(struct_tagNET_VCA_ONE_RULE_V41, [
    ('byActive', BYTE),
    ('byRes1', BYTE * 4),
    ('byEventTypeFlag', BYTE),
    ('wEventTypeEx', WORD),
    ('byRuleName', BYTE * 32),
    ('dwEventType', VCA_EVENT_TYPE),
    ('uEventParam', NET_VCA_EVENT_UNION),
    ('struSizeFilter', NET_VCA_SIZE_FILTER),
    ('struAlarmTime', (NET_DVR_SCHEDTIME * 8) * 7),
    ('struHandleType', NET_DVR_HANDLEEXCEPTION_V30),
    ('byRelRecordChan', BYTE * int((32 + 32))),
    ('wAlarmDelay', WORD),
    ('byRes2', BYTE * 2),
    ('struFilterStrategy', NET_VCA_FILTER_STRATEGY),
    ('struTriggerParam', NET_VCA_RULE_TRIGGER_PARAM),
    ('byRes', BYTE * 32),
])

NET_VCA_ONE_RULE_V41 = struct_tagNET_VCA_ONE_RULE_V41
LPNET_VCA_ONE_RULE_V41 = POINTER(struct_tagNET_VCA_ONE_RULE_V41)
tagNET_VCA_ONE_RULE_V41 = struct_tagNET_VCA_ONE_RULE_V41
