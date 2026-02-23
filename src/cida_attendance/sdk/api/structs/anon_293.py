from ctypes import Union

from ..base_classes import _S, BYTE
from .anon_291 import struct_anon_291
from .anon_292 import struct_anon_292


class union_anon_293(Union):
    pass

_S(union_anon_293, [
    ('Res', BYTE * 200),
    ('struDecoderSystemAbility', struct_anon_291),
    ('struCoderSystemAbility', struct_anon_292),
])

