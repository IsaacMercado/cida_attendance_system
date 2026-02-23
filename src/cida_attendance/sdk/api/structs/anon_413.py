from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_anon_413(Structure):
    pass

_S(struct_anon_413, [
    ('sData', BYTE * 128),
    ('byExclusive', BYTE),
    ('byFlagType', BYTE),
    ('byRes', BYTE * 6),
])

NET_DVR_GENERIC_END = struct_anon_413
LPNET_DVR_GENERIC_END = POINTER(struct_anon_413)
