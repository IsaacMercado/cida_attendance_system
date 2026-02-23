from ctypes import Union

from ..base_classes import _S, BYTE
from .anon_398 import struct_anon_398


class union_anon_399(Union):
    pass

_S(union_anon_399, [
    ('uLen', BYTE * 128),
    ('struVehicleInfo', struct_anon_398),
])

