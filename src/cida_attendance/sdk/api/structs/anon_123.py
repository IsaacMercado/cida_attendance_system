from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .anon_122 import NET_DVR_DECINFO


class struct_anon_123(Structure):
    pass

_S(struct_anon_123, [
    ('dwSize', DWORD),
    ('dwDecChanNum', DWORD),
    ('struDecInfo', NET_DVR_DECINFO * 4),
])

NET_DVR_DECCFG = struct_anon_123
LPNET_DVR_DECCFG = POINTER(struct_anon_123)
