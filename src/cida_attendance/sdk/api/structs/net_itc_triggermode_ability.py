from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_ITC_TRIGGERMODE_ABILITY(Structure):
    pass

_S(struct_tagNET_ITC_TRIGGERMODE_ABILITY, [
    ('dwSize', DWORD),
    ('dwTriggerType', DWORD),
    ('byRes', BYTE * 16),
])

NET_ITC_TRIGGERMODE_ABILITY = struct_tagNET_ITC_TRIGGERMODE_ABILITY
LPNET_ITC_TRIGGERMODE_ABILITY = POINTER(struct_tagNET_ITC_TRIGGERMODE_ABILITY)
tagNET_ITC_TRIGGERMODE_ABILITY = struct_tagNET_ITC_TRIGGERMODE_ABILITY
