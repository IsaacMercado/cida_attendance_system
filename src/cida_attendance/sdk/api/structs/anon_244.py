from ctypes import Structure

from ..base_classes import _S, BYTE, WORD


class struct_anon_244(Structure):
    pass

_S(struct_anon_244, [
    ('wMotDetChanNo', WORD * int((32 + 32))),
    ('byRes', BYTE * 672),
])

