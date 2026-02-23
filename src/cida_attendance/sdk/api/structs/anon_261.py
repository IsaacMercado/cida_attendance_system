from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD


class struct_anon_261(Structure):
    pass

_S(struct_anon_261, [
    ('dwMajor', DWORD),
    ('dwMinor', DWORD),
    ('byCardNo', BYTE * 32),
    ('byName', BYTE * 32),
    ('byMACAddr', BYTE * 6),
    ('byRes', BYTE * 722),
])

