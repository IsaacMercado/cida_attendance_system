from ctypes import Structure

from ..base_classes import _S, BYTE
from .anon_212 import union_anon_212


class struct_anon_213(Structure):
    pass

_S(struct_anon_213, [
    ('byEncryptType', BYTE),
    ('byAuthType', BYTE),
    ('byRes', BYTE * 2),
    ('auth_param', union_anon_212),
])

