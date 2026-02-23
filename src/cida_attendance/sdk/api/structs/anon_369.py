from ctypes import Union

from ..base_classes import _S
from .anon_367 import struct_anon_367
from .anon_368 import struct_anon_368


class union_anon_369(Union):
    pass

_S(union_anon_369, [
    ('struDomain', struct_anon_367),
    ('struAddrIP', struct_anon_368),
])

