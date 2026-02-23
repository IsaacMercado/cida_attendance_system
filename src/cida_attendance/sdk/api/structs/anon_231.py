from ctypes import Structure

from ..base_classes import _S, BYTE


class struct_anon_231(Structure):
    pass

_S(struct_anon_231, [
    ('byAlarmInNo', BYTE * int((32 + 128))),
    ('byRes', BYTE * int((300 - (32 + 128)))),
])

