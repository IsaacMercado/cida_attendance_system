from ctypes import Structure

from ..base_classes import _S, BYTE


class struct_anon_370(Structure):
    pass

_S(struct_anon_370, [
    ('szDomain', BYTE * 64),
    ('byRes1', BYTE * 80),
])

