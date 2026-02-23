from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .anon_135 import NET_DVR_SHOWSTRINGINFO


class struct_anon_137(Structure):
    pass

_S(struct_anon_137, [
    ('dwSize', DWORD),
    ('struStringInfo', NET_DVR_SHOWSTRINGINFO * 8),
])

NET_DVR_SHOWSTRING_EX = struct_anon_137
LPNET_DVR_SHOWSTRING_EX = POINTER(struct_anon_137)
