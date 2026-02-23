from ctypes import Union

from ..base_classes import _S, BYTE
from .anon_429 import struct_anon_429


class union_anon_430(Union):
    pass

_S(union_anon_430, [
    ('byUnionLen', BYTE * 128),
    ('struStrobeLamp', struct_anon_429),
])

