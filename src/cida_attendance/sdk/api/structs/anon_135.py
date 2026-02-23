from ctypes import Structure, c_char

from ..base_classes import _S, WORD
from ..ctypes_preamble import POINTER


class struct_anon_135(Structure):
    pass

_S(struct_anon_135, [
    ('wShowString', WORD),
    ('wStringSize', WORD),
    ('wShowStringTopLeftX', WORD),
    ('wShowStringTopLeftY', WORD),
    ('sString', c_char * 44),
])

NET_DVR_SHOWSTRINGINFO = struct_anon_135
LPNET_DVR_SHOWSTRINGINFO = POINTER(struct_anon_135)
