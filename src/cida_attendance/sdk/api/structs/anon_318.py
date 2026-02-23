from ctypes import Union

from ..base_classes import _S, BYTE
from .anon_316 import struct_anon_316
from .anon_317 import struct_anon_317


class union_anon_318(Union):
    pass

_S(union_anon_318, [
    ('byRes', BYTE * 160),
    ('struVideoPlatform', struct_anon_316),
    ('struNotVideoPlatform', struct_anon_317),
])

