from ctypes import Structure

from ..base_classes import _S, BYTE


class struct_anon_235(Structure):
    pass

_S(struct_anon_235, [
    ('byChanNo', BYTE * int((32 + 32))),
    ('byRuleID', BYTE),
    ('byRes1', BYTE * 43),
])

