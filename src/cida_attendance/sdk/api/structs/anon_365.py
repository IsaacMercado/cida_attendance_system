from ctypes import Structure

from ..base_classes import _S, BYTE


class struct_anon_365(Structure):
    pass

_S(struct_anon_365, [
    ('byRes1', BYTE * 228),
    ('byDiskNumber', BYTE * 33),
    ('byDeviceID', BYTE * 32),
    ('byRes2', BYTE * 7),
])

