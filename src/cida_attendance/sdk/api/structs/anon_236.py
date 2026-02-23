from ctypes import Structure

from ..base_classes import _S, BYTE, WORD


class struct_anon_236(Structure):
    pass

_S(struct_anon_236, [
    ('wChanNo', WORD * 64),
    ('byRuleID', BYTE),
    ('byRes', BYTE * 171),
])

