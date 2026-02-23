from ctypes import Union, c_char

from ..base_classes import _S
from .anon_327 import struct_anon_327


class union_anon_328(Union):
    pass

_S(union_anon_328, [
    ('sFileName', c_char * 100),
    ('struPlayBackbyTime', struct_anon_327),
])

