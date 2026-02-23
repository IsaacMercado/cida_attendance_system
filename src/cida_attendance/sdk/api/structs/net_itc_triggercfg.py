from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_itc_single_triggercfg import NET_ITC_SINGLE_TRIGGERCFG


class struct_tagNET_ITC_TRIGGERCFG(Structure):
    pass

_S(struct_tagNET_ITC_TRIGGERCFG, [
    ('dwSize', DWORD),
    ('struTriggerParam', NET_ITC_SINGLE_TRIGGERCFG),
    ('byRes', BYTE * 32),
])

NET_ITC_TRIGGERCFG = struct_tagNET_ITC_TRIGGERCFG
LPNET_ITC_TRIGGERCFG = POINTER(struct_tagNET_ITC_TRIGGERCFG)
tagNET_ITC_TRIGGERCFG = struct_tagNET_ITC_TRIGGERCFG
