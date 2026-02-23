from ctypes import Union

from ..base_classes import _S, BYTE
from .anon_370 import struct_anon_370
from .anon_371 import struct_anon_371


class union_anon_372(Union):
    pass

_S(union_anon_372, [
    ('byRes', BYTE * 144),
    ('struDomain', struct_anon_370),
    ('struAddrIP', struct_anon_371),
])

