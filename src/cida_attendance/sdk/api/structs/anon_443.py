from ctypes import Union

from ..base_classes import _S
from .anon_441 import struct_anon_441
from .anon_442 import struct_anon_442


class union_anon_443(Union):
    pass

_S(union_anon_443, [
    ('struDomain', struct_anon_441),
    ('struAddrIP', struct_anon_442),
])

