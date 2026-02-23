from ctypes import Union

from ..base_classes import _S, BYTE
from .anon_425 import struct_anon_425
from .anon_426 import struct_anon_426
from .anon_427 import struct_anon_427


class union_anon_428(Union):
    pass

_S(union_anon_428, [
    ('byUnionLen', BYTE * 656),
    ('struRrReader', struct_anon_425),
    ('struGateway', struct_anon_426),
    ('struLed', struct_anon_427),
])

