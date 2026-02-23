from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_anon_188(Structure):
    pass

_S(struct_anon_188, [
    ('dwSize', DWORD),
    ('wPort', WORD),
    ('byReserve1', BYTE * 40),
    ('wRtspsPort', WORD),
    ('byReserve', BYTE * 12),
])

NET_DVR_RTSPCFG = struct_anon_188
LPNET_DVR_RTSPCFG = POINTER(struct_anon_188)
