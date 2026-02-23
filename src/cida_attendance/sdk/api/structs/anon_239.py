from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD


class struct_anon_239(Structure):
    pass

_S(struct_anon_239, [
    ('dwChanNo', DWORD * int(((32 + 32) - 1))),
    ('byAll', BYTE),
    ('byres', BYTE * 3),
])

