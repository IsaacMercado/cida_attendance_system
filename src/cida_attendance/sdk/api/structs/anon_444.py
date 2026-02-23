from ctypes import Structure

from ..base_classes import _S, BYTE


class struct_anon_444(Structure):
    pass

_S(struct_anon_444, [
    ('szDomain', BYTE * 64),
    ('byRes2', BYTE * 80),
])

