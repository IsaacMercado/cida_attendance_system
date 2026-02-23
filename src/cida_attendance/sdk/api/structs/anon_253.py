from ctypes import Structure

from ..base_classes import _S, BYTE, WORD


class struct_anon_253(Structure):
    pass

_S(struct_anon_253, [
    ('wAlarmInNo', WORD * 128),
    ('byRes', BYTE * 544),
])

