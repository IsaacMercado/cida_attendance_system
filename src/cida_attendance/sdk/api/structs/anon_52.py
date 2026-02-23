from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .anon_49 import NET_DVR_PPPCFG_V30
from .anon_51 import NET_DVR_SINGLE_RS232


class struct_anon_52(Structure):
    pass

_S(struct_anon_52, [
    ('dwSize', DWORD),
    ('struRs232', NET_DVR_SINGLE_RS232 * 8),
    ('struPPPConfig', NET_DVR_PPPCFG_V30),
])

NET_DVR_RS232CFG_V30 = struct_anon_52
LPNET_DVR_RS232CFG_V30 = POINTER(struct_anon_52)
