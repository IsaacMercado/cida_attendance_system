from ctypes import Structure, c_char

from ..base_classes import _S, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_anon_124(Structure):
    pass

_S(struct_anon_124, [
    ('dwEnableTransPort', DWORD),
    ('sDecoderIP', c_char * 16),
    ('wDecoderPort', WORD),
    ('wDVRTransPort', WORD),
    ('cReserve', c_char * 4),
])

NET_DVR_PORTINFO = struct_anon_124
LPNET_DVR_PORTINFO = POINTER(struct_anon_124)
