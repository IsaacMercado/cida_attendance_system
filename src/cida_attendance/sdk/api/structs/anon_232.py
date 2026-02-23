from ctypes import Structure

from ..base_classes import _S, BYTE, WORD


class struct_anon_232(Structure):
    pass

_S(struct_anon_232, [
    ('wAlarmInNo', WORD * 128),
    ('byRes', BYTE * 44),
])

