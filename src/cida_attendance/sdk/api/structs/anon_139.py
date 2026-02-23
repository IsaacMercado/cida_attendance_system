from ctypes import Structure

from ..base_classes import _S, BYTE


class struct_anon_139(Structure):
    pass

_S(struct_anon_139, [
    ('sName', BYTE * 32),
    ('sAddress', BYTE * 48),
])

