from ctypes import Union

from ..base_classes import _S, BYTE
from .anon_180 import struct_anon_180
from .anon_181 import struct_anon_181


class union_anon_182(Union):
    pass

_S(union_anon_182, [
    ('byRes', BYTE * 16),
    ('struVideoPlatform', struct_anon_180),
    ('struNotVideoPlatform', struct_anon_181),
])

