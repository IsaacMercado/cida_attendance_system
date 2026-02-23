from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD


class struct_anon_283(Structure):
    pass

_S(struct_anon_283, [
    ('dwChanNo', DWORD),
    ('byRes', BYTE * 796),
])

