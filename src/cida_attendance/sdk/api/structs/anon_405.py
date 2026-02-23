from ctypes import Structure, c_int

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_anon_405(Structure):
    pass

_S(struct_anon_405, [
    ('iWeight', c_int),
    ('byRes', BYTE * 508),
])

NET_DVR_WEIGHT_STATE = struct_anon_405
LPNET_DVR_WEIGHT_STATE = POINTER(struct_anon_405)
