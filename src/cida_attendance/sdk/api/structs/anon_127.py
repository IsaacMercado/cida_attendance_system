from ctypes import Union

from ..base_classes import _S, BYTE
from .anon_126 import struct_anon_126


class union_anon_127(Union):
    pass

_S(union_anon_127, [
    ('byFile', BYTE * 100),
    ('bytime', struct_anon_126),
])

