from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from .net_vca_event_union import NET_VCA_EVENT_UNION


class struct_anon_273(Structure):
    pass

_S(struct_anon_273, [
    ('dwChanNo', DWORD),
    ('byRuleID', BYTE),
    ('byRes1', BYTE * 3),
    ('byRuleName', BYTE * 32),
    ('uEvent', NET_VCA_EVENT_UNION),
    ('byRes', BYTE * 668),
])

