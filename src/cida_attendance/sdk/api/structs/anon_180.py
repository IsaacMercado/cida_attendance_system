from ctypes import Structure

from ..base_classes import _S, BYTE


class struct_anon_180(Structure):
    pass

_S(struct_anon_180, [
    ('byJoinDecoderId', BYTE * 16),
])

