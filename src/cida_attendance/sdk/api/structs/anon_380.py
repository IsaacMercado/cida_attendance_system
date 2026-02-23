from ctypes import Structure

from ..base_classes import _S, BYTE


class struct_anon_380(Structure):
    pass

_S(struct_anon_380, [
    ('byPhoneNum', BYTE * 32),
    ('byRes1', BYTE * 708),
])

