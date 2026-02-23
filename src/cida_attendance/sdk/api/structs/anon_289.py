from ctypes import Union

from ..base_classes import _S
from .anon_287 import struct_anon_287
from .anon_288 import struct_anon_288


class union_anon_289(Union):
    pass

_S(union_anon_289, [
    ('struStatFrame', struct_anon_287),
    ('struStatTime', struct_anon_288),
])

