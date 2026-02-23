from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD


class struct_anon_272(Structure):
    pass

_S(struct_anon_272, [
    ('dwMotDetNo', DWORD),
    ('byRes', BYTE * 796),
])

