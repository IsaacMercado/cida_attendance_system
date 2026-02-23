from ctypes import Union

from ..base_classes import _S
from .anon_343 import struct_anon_343
from .anon_344 import struct_anon_344


class union_anon_345(Union):
    pass

_S(union_anon_345, [
    ('struDomain', struct_anon_343),
    ('struAddrIP', struct_anon_344),
])

