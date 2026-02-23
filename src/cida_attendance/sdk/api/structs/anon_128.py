from ctypes import Structure, c_char

from ..base_classes import _S, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_127 import union_anon_127


class struct_anon_128(Structure):
    pass

_S(struct_anon_128, [
    ('dwSize', DWORD),
    ('sDecoderIP', c_char * 16),
    ('wDecoderPort', WORD),
    ('wLoadMode', WORD),
    ('mode_size', union_anon_127),
])

NET_DVR_PLAYREMOTEFILE = struct_anon_128
LPNET_DVR_PLAYREMOTEFILE = POINTER(struct_anon_128)
