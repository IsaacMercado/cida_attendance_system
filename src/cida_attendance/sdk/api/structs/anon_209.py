from ctypes import Structure

from ..base_classes import _S, BYTE


class struct_anon_209(Structure):
    pass

_S(struct_anon_209, [
    ('byEapolVersion', BYTE),
    ('byAuthType', BYTE),
    ('byRes1', BYTE * 2),
    ('byAnonyIdentity', BYTE * 32),
    ('byUserName', BYTE * 32),
    ('byPassword', BYTE * 32),
    ('byRes', BYTE * 44),
])

