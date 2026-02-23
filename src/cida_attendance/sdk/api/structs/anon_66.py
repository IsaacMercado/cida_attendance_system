from ctypes import Structure, c_float

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_anon_66(Structure):
    pass

_S(struct_anon_66, [
    ('fTemperature', c_float),
    ('dwCustomInfoLength', DWORD),
    ('pCustomInfo', POINTER(BYTE)),
    ('byType', BYTE),
    ('byDeicingEnabled', BYTE),
    ('byRes2', BYTE * 2),
    ('dwChannel', DWORD),
])

