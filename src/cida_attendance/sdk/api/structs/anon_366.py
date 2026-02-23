from ctypes import Union

from ..base_classes import _S, BYTE
from .anon_363 import struct_anon_363
from .anon_364 import struct_anon_364
from .anon_365 import struct_anon_365


class union_anon_366(Union):
    pass

_S(union_anon_366, [
    ('byRes', BYTE * 300),
    ('struIOAlarm', struct_anon_363),
    ('struStreamIDorChannel', struct_anon_364),
    ('struDiskAlarm', struct_anon_365),
])

