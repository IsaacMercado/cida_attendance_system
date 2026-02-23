from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from ..enums import VCA_EVENT_TYPE
from .anon_6 import NET_DVR_SCHEDTIME
from .anon_7 import NET_DVR_HANDLEEXCEPTION_V30
from .net_vca_event_union import NET_VCA_EVENT_UNION
from .net_vca_size_filter import NET_VCA_SIZE_FILTER


class struct_tagNET_VCA_ONE_RULE(Structure):
    pass

_S(struct_tagNET_VCA_ONE_RULE, [
    ('byActive', BYTE),
    ('byRes', BYTE * 7),
    ('byRuleName', BYTE * 32),
    ('dwEventType', VCA_EVENT_TYPE),
    ('uEventParam', NET_VCA_EVENT_UNION),
    ('struSizeFilter', NET_VCA_SIZE_FILTER),
    ('struAlarmTime', (NET_DVR_SCHEDTIME * 2) * 7),
    ('struHandleType', NET_DVR_HANDLEEXCEPTION_V30),
    ('byRelRecordChan', BYTE * int((32 + 32))),
])

NET_VCA_ONE_RULE = struct_tagNET_VCA_ONE_RULE
LPNET_VCA_ONE_RULE = POINTER(struct_tagNET_VCA_ONE_RULE)
tagNET_VCA_ONE_RULE = struct_tagNET_VCA_ONE_RULE
