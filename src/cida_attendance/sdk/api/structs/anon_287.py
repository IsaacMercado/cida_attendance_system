from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD


class struct_anon_287(Structure):
    pass

_S(struct_anon_287, [
    ('dwRelativeTime', DWORD),
    ('dwAbsTime', DWORD),
    ('byTimeDiffFlag', BYTE),
    ('cTimeDifferenceH', c_char),
    ('cTimeDifferenceM', c_char),
    ('byRes', BYTE * 89),
])

