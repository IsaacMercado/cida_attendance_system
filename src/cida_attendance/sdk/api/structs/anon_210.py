from ctypes import Structure

from ..base_classes import _S, BYTE


class struct_anon_210(Structure):
    pass

_S(struct_anon_210, [
    ('byEapolVersion', BYTE),
    ('byAuthType', BYTE),
    ('byPeapVersion', BYTE),
    ('byPeapLabel', BYTE),
    ('byAnonyIdentity', BYTE * 32),
    ('byUserName', BYTE * 32),
    ('byPassword', BYTE * 32),
    ('byRes', BYTE * 44),
])

