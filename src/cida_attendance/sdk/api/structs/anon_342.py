from ctypes import Union

from ..base_classes import _S, BYTE
from .anon_340 import struct_anon_340
from .anon_341 import struct_anon_341


class union_anon_342(Union):
    pass

_S(union_anon_342, [
    ('uLen', BYTE * 4),
    ('struIO', struct_anon_340),
    ('struRS485', struct_anon_341),
])

