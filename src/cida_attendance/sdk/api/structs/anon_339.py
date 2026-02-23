from ctypes import Union

from ..base_classes import _S, BYTE
from .anon_337 import struct_anon_337
from .anon_338 import struct_anon_338


class union_anon_339(Union):
    pass

_S(union_anon_339, [
    ('uLen', BYTE * 4),
    ('struIO', struct_anon_337),
    ('struRS485', struct_anon_338),
])

