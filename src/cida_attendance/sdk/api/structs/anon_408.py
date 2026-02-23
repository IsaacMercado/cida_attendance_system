from ctypes import Structure, c_int

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_anon_408(Structure):
    pass

_S(struct_anon_408, [
    ('iNatrualGasThick', c_int),
    ('byRes', BYTE * 508),
])

NET_DVR_FUEL_GAS_DETE_STATE = struct_anon_408
LPNET_DVR_FUEL_GAS_DETE_STATE = POINTER(struct_anon_408)
