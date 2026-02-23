from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_anon_414(Structure):
    pass

_S(struct_anon_414, [
    ('sData', BYTE * 128),
    ('byFlagType', BYTE),
    ('byRes', BYTE * 3),
])

NET_DVR_GENERIC_DATA_CFG = struct_anon_414
LPNET_DVR_GENERIC_DATA_CFG = POINTER(struct_anon_414)
