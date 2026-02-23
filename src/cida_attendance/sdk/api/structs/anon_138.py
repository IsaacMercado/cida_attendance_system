from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .anon_135 import NET_DVR_SHOWSTRINGINFO


class struct_anon_138(Structure):
    pass

_S(struct_anon_138, [
    ('dwSize', DWORD),
    ('struStringInfo', NET_DVR_SHOWSTRINGINFO * 4),
])

NET_DVR_SHOWSTRING = struct_anon_138
LPNET_DVR_SHOWSTRING = POINTER(struct_anon_138)
