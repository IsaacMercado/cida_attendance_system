from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_event_param_union import NET_DVR_EVENT_PARAM_UNION


class struct_tagNET_DVR_EVENT_INFO(Structure):
    pass

_S(struct_tagNET_DVR_EVENT_INFO, [
    ('byRuleID', BYTE),
    ('byRes', BYTE * 3),
    ('byRuleName', BYTE * 32),
    ('dwEventType', DWORD),
    ('uEventParam', NET_DVR_EVENT_PARAM_UNION),
])

NET_DVR_EVENT_INFO = struct_tagNET_DVR_EVENT_INFO
LPNET_DVR_EVENT_INFO = POINTER(struct_tagNET_DVR_EVENT_INFO)
tagNET_DVR_EVENT_INFO = struct_tagNET_DVR_EVENT_INFO
