from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from ..enums import VCA_EVENT_TYPE
from .net_vca_event_union import NET_VCA_EVENT_UNION
from .net_vca_size_filter import NET_VCA_SIZE_FILTER


class struct_tagNET_IVMS_ONE_RULE_(Structure):
    pass

_S(struct_tagNET_IVMS_ONE_RULE_, [
    ('byActive', BYTE),
    ('byRes1', BYTE * 7),
    ('byRuleName', BYTE * 32),
    ('dwEventType', VCA_EVENT_TYPE),
    ('uEventParam', NET_VCA_EVENT_UNION),
    ('struSizeFilter', NET_VCA_SIZE_FILTER),
    ('byRes2', BYTE * 68),
])

NET_IVMS_ONE_RULE = struct_tagNET_IVMS_ONE_RULE_
LPNET_IVMS_ONE_RULE = POINTER(struct_tagNET_IVMS_ONE_RULE_)
tagNET_IVMS_ONE_RULE_ = struct_tagNET_IVMS_ONE_RULE_
