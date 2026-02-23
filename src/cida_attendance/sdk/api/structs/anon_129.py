from ctypes import Structure, c_char

from ..base_classes import _S, BYTE


class struct_anon_129(Structure):
    pass

_S(struct_anon_129, [
    ('sUserName', BYTE * 32),
    ('sPassword', BYTE * 16),
    ('cReserve', c_char * 52),
])

