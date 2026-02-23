from ctypes import Structure

from ..base_classes import _S, BYTE, WORD


class struct_anon_243(Structure):
    pass

_S(struct_anon_243, [
    ('wAlarmInNo', WORD * 128),
    ('byRes', BYTE * 544),
])

