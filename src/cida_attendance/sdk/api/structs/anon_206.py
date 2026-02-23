from ctypes import Structure, c_int

from ..base_classes import _S
from ..ctypes_preamble import POINTER


class struct_anon_206(Structure):
    pass

_S(struct_anon_206, [
    ('xTop', c_int),
    ('yTop', c_int),
    ('xBottom', c_int),
    ('yBottom', c_int),
    ('bCounter', c_int),
])

NET_DVR_POINT_FRAME = struct_anon_206
LPNET_DVR_POINT_FRAME = POINTER(struct_anon_206)
