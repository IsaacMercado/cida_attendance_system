from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_6 import NET_DVR_SCHEDTIME
from .net_dvr_handleexception_v40 import NET_DVR_HANDLEEXCEPTION_V40
from .net_vca_event_union import NET_VCA_EVENT_UNION
from .net_vca_filter_strategy import NET_VCA_FILTER_STRATEGY
from .net_vca_rule_trigger_param import NET_VCA_RULE_TRIGGER_PARAM
from .net_vca_size_filter import NET_VCA_SIZE_FILTER


class struct_NET_VCA_ONE_RULE_V42_(Structure):
    pass

_S(struct_NET_VCA_ONE_RULE_V42_, [
    ('byActive', BYTE),
    ('byEventPriority', BYTE),
    ('byBackgroundSuppression', BYTE),
    ('byRes1', BYTE * 3),
    ('wEventType', WORD),
    ('byRuleName', BYTE * 32),
    ('uEventParam', NET_VCA_EVENT_UNION),
    ('struSizeFilter', NET_VCA_SIZE_FILTER),
    ('struAlarmTime', (NET_DVR_SCHEDTIME * 8) * 7),
    ('struAlarmHandleType', NET_DVR_HANDLEEXCEPTION_V40),
    ('dwRelRecordChan', DWORD * int((32 + 32))),
    ('wAlarmDelay', WORD),
    ('byRes2', BYTE * 2),
    ('struFilterStrategy', NET_VCA_FILTER_STRATEGY),
    ('struTriggerParam', NET_VCA_RULE_TRIGGER_PARAM),
    ('byRes', BYTE * 32),
])

NET_VCA_ONE_RULE_V42 = struct_NET_VCA_ONE_RULE_V42_
LPNET_VCA_ONE_RULE_V42 = POINTER(struct_NET_VCA_ONE_RULE_V42_)
NET_VCA_ONE_RULE_V42_ = struct_NET_VCA_ONE_RULE_V42_
