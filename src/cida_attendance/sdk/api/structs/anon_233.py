from ctypes import Structure

from ..base_classes import _S, BYTE


class struct_anon_233(Structure):
    pass

_S(struct_anon_233, [
    ('byMotDetChanNo', BYTE * int((32 + 32))),
    ('byRes', BYTE * int((300 - (32 + 32)))),
])

