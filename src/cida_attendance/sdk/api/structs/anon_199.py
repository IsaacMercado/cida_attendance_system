from ctypes import Structure, c_long

from ..base_classes import _S
from ..ctypes_preamble import POINTER


class struct_anon_199(Structure):
    pass

_S(struct_anon_199, [
    ('bToScreen', c_long),
    ('bToVideoOut', c_long),
    ('nLeft', c_long),
    ('nTop', c_long),
    ('nWidth', c_long),
    ('nHeight', c_long),
    ('nReserved', c_long),
])

NET_DVR_DISPLAY_PARA = struct_anon_199
LPNET_DVR_DISPLAY_PARA = POINTER(struct_anon_199)
