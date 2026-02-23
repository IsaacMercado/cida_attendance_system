from ctypes import Structure

from ..base_classes import _S, BYTE, WORD


class struct_anon_257(Structure):
    pass

_S(struct_anon_257, [
    ('byAll', BYTE),
    ('byRes1', BYTE * 3),
    ('wChanNo', WORD * int((32 + 32))),
])

