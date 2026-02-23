from ctypes import Union

from ..base_classes import _S
from .anon_207 import struct_anon_207
from .anon_208 import struct_anon_208
from .anon_213 import struct_anon_213


class union_anon_214(Union):
    pass

_S(union_anon_214, [
    ('wep', struct_anon_207),
    ('wpa_psk', struct_anon_208),
    ('wpa_wpa2', struct_anon_213),
])

