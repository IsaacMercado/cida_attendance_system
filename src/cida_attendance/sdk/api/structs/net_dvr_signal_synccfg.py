from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SIGNAL_SYNCCFG(Structure):
    pass

_S(struct_tagNET_DVR_SIGNAL_SYNCCFG, [
    ('dwSize', DWORD),
    ('wPhase', WORD),
    ('byLineLock', BYTE),
    ('byRes', BYTE * 125),
])

NET_DVR_SIGNAL_SYNCCFG = struct_tagNET_DVR_SIGNAL_SYNCCFG
LPNET_DVR_SIGNAL_SYNCCFG = POINTER(struct_tagNET_DVR_SIGNAL_SYNCCFG)
tagNET_DVR_SIGNAL_SYNCCFG = struct_tagNET_DVR_SIGNAL_SYNCCFG
