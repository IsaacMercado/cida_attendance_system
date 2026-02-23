from ctypes import Structure, c_float

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_anon_453(Structure):
    pass

_S(struct_anon_453, [
    ('fPanPos', c_float),
    ('fTiltPos', c_float),
    ('fZoomPos', c_float),
    ('byRes', BYTE * 16),
])

NET_DVR_PTZPOS_PARAM = struct_anon_453
LPNET_DVR_PTZPOS_PARAM = POINTER(struct_anon_453)
