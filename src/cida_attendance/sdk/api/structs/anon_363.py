from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD


class struct_anon_363(Structure):
    pass

_S(struct_anon_363, [
    ('dwAlarmInputNumber', DWORD),
    ('byAlarmOutputNumber', BYTE * int((32 + 64))),
    ('byAlarmRelateChannel', BYTE * int((32 + 32))),
    ('byRes1', BYTE * 97),
    ('byDeviceID', BYTE * 32),
    ('byRes2', BYTE * 7),
])

