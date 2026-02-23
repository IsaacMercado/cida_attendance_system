from ctypes import Union

from ..base_classes import _S
from .anon_228 import struct_anon_228
from .anon_229 import struct_anon_229


class union_anon_230(Union):
    pass

_S(union_anon_230, [
    ('struDomain', struct_anon_228),
    ('struAddrIP', struct_anon_229),
])

