from ctypes import Union

from ..base_classes import _S, BYTE
from .anon_450 import struct_anon_450
from .anon_451 import struct_anon_451


class union_anon_452(Union):
    pass

_S(union_anon_452, [
    ('byLen', BYTE * 512),
    ('struChannelInfo', struct_anon_450),
    ('struAddrInfo', struct_anon_451),
])

