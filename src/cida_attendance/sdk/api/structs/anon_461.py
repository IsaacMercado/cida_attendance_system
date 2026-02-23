from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD


class struct_anon_461(Structure):
    pass

_S(struct_anon_461, [
    ('dwPlayItem', DWORD),
    ('byPlayItemName', BYTE * 32),
    ('byRes2', BYTE * 8),
])

