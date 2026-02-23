from ctypes import Union

from ..base_classes import _S
from .anon_352 import struct_anon_352
from .anon_353 import struct_anon_353


class union_anon_354(Union):
    pass

_S(union_anon_354, [
    ('TimeSeg', struct_anon_352),
    ('TimePoint', struct_anon_353),
])

