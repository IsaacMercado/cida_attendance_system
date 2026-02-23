from ctypes import Union, c_char

from ..base_classes import _S
from .anon_329 import struct_anon_329


class union_anon_330(Union):
    pass

_S(union_anon_330, [
    ('sFileName', c_char * 100),
    ('struPlayBackbyTime', struct_anon_329),
])

