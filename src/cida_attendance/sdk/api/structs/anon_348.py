from ctypes import Union

from ..base_classes import _S
from .anon_346 import struct_anon_346
from .anon_347 import struct_anon_347


class union_anon_348(Union):
    pass

_S(union_anon_348, [
    ('struDomain', struct_anon_346),
    ('struAddrIP', struct_anon_347),
])

