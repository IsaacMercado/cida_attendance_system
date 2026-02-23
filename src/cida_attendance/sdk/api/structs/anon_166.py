from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_anon_166(Structure):
    pass

_S(struct_anon_166, [
    ('baudrate', BYTE),
    ('databits', BYTE),
    ('stopbits', BYTE),
    ('parity', BYTE),
    ('flowcontrol', BYTE),
    ('res', BYTE * 3),
])

TTY_CONFIG = struct_anon_166
LPTTY_CONFIG = POINTER(struct_anon_166)
