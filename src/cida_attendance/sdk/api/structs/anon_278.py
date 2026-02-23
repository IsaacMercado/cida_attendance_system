from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD


class struct_anon_278(Structure):
    pass

_S(struct_anon_278, [
    ('dwAlarmInNo', DWORD),
    ('byRes', BYTE * 796),
])

