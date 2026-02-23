from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_itc_trigger_param_union import NET_ITC_TRIGGER_PARAM_UNION


class struct_tagNET_ITC_SINGLE_TRIGGERCFG(Structure):
    pass

_S(struct_tagNET_ITC_SINGLE_TRIGGERCFG, [
    ('byEnable', BYTE),
    ('byRes1', BYTE * 3),
    ('dwTriggerType', DWORD),
    ('uTriggerParam', NET_ITC_TRIGGER_PARAM_UNION),
    ('byRes', BYTE * 64),
])

NET_ITC_SINGLE_TRIGGERCFG = struct_tagNET_ITC_SINGLE_TRIGGERCFG
LPNET_ITC_SINGLE_TRIGGERCFG = POINTER(struct_tagNET_ITC_SINGLE_TRIGGERCFG)
tagNET_ITC_SINGLE_TRIGGERCFG = struct_tagNET_ITC_SINGLE_TRIGGERCFG
