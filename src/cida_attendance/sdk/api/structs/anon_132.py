from ctypes import Union

from ..base_classes import _S
from .anon_129 import struct_anon_129
from .anon_130 import struct_anon_130
from .anon_131 import struct_anon_131


class union_anon_132(Union):
    pass

_S(union_anon_132, [
    ('userInfo', struct_anon_129),
    ('fileInfo', struct_anon_130),
    ('timeInfo', struct_anon_131),
])

