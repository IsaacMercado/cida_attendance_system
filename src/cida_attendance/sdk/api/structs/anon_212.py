from ctypes import Union

from ..base_classes import _S
from .anon_209 import struct_anon_209
from .anon_210 import struct_anon_210
from .anon_211 import struct_anon_211


class union_anon_212(Union):
    pass

_S(union_anon_212, [
    ('EAP_TTLS', struct_anon_209),
    ('EAP_PEAP', struct_anon_210),
    ('EAP_TLS', struct_anon_211),
])

