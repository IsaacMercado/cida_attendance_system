from ctypes import Structure

from ..base_classes import _S, BYTE


class struct_anon_338(Structure):
    pass

_S(struct_anon_338, [
    ('byRelateChan', BYTE),
    ('byRes2', BYTE * 3),
])

