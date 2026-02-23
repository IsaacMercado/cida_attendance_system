from ctypes import Union

from ..base_classes import _S, BYTE
from .anon_455 import struct_anon_455
from .anon_456 import struct_anon_456
from .anon_457 import struct_anon_457


class union_anon_458(Union):
    pass

_S(union_anon_458, [
    ('uLen', BYTE * 32),
    ('struScale', struct_anon_455),
    ('struQuality', struct_anon_456),
    ('struResolution', struct_anon_457),
])

