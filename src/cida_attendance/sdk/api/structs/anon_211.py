from ctypes import Structure

from ..base_classes import _S, BYTE


class struct_anon_211(Structure):
    pass

_S(struct_anon_211, [
    ('byEapolVersion', BYTE),
    ('byRes1', BYTE * 3),
    ('byIdentity', BYTE * 32),
    ('byPrivateKeyPswd', BYTE * 32),
    ('byRes', BYTE * 76),
])

