from ctypes import Structure

from ..base_classes import _S, BYTE, WORD


class struct_anon_234(Structure):
    pass

_S(struct_anon_234, [
    ('wMotDetChanNo', WORD * 64),
    ('byRes', BYTE * 172),
])

