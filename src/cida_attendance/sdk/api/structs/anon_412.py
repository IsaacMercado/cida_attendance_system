from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_anon_412(Structure):
    pass

_S(struct_anon_412, [
    ('sData', BYTE * 128),
    ('byExclusive', BYTE),
    ('byFlagType', BYTE),
    ('byRes', BYTE * 2),
])

NET_DVR_GENERIC_START = struct_anon_412
LPNET_DVR_GENERIC_START = POINTER(struct_anon_412)
