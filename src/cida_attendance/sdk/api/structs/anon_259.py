from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, WORD


class struct_anon_259(Structure):
    pass

_S(struct_anon_259, [
    ('wChannel', WORD * int((32 + 32))),
    ('byAllChan', BYTE),
    ('byCaseSensitive', BYTE),
    ('byCombinateMode', BYTE),
    ('byRes1', BYTE),
    ('sKeyWord', (c_char * 128) * 3),
    ('byRes', BYTE * 284),
])

