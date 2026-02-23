from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_anon_460(Structure):
    pass

_S(struct_anon_460, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('byRes', BYTE * 128),
])

NET_DVR_SHIPSCOUNT_COND = struct_anon_460
LPNET_DVR_SHIPSCOUNT_COND = POINTER(struct_anon_460)
