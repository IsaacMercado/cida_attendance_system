from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD


class struct_anon_265(Structure):
    pass

_S(struct_anon_265, [
    ('dwMotDetNo', DWORD),
    ('byRes', BYTE * 300),
])

