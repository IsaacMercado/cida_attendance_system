from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD


class struct_anon_264(Structure):
    pass

_S(struct_anon_264, [
    ('dwAlarmInNo', DWORD),
    ('byRes', BYTE * 300),
])

