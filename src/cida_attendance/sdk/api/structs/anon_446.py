from ctypes import Union

from ..base_classes import _S
from .anon_444 import struct_anon_444
from .anon_445 import struct_anon_445


class union_anon_446(Union):
    pass

_S(union_anon_446, [
    ('struDomain', struct_anon_444),
    ('struAddrIP', struct_anon_445),
])

