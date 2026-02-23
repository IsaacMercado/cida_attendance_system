from ctypes import Structure

from ..base_classes import _S, BYTE


class struct_anon_364(Structure):
    pass

_S(struct_anon_364, [
    ('byStreamID', BYTE * 32),
    ('byRes1', BYTE * 132),
    ('byChannel', BYTE * int((32 + 32))),
    ('byRes2', BYTE * 33),
    ('byDeviceID', BYTE * 32),
    ('byRes3', BYTE * 7),
])

