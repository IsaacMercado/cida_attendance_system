from ctypes import Structure

from ..base_classes import _S, BYTE


class struct_anon_316(Structure):
    pass

_S(struct_anon_316, [
    ('byJoinDecoderId', BYTE * 16),
    ('byDecResolution', BYTE),
    ('byRes', BYTE * 143),
])

