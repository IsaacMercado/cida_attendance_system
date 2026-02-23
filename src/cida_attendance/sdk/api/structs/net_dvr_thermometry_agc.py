from ctypes import Structure, c_int

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_THERMOMETRY_AGC(Structure):
    pass

_S(struct_tagNET_DVR_THERMOMETRY_AGC, [
    ('byMode', BYTE),
    ('byRes1', BYTE * 3),
    ('iHighTemperature', c_int),
    ('iLowTemperature', c_int),
    ('byRes', BYTE * 8),
])

NET_DVR_THERMOMETRY_AGC = struct_tagNET_DVR_THERMOMETRY_AGC
LPNET_DVR_THERMOMETRY_AGC = POINTER(struct_tagNET_DVR_THERMOMETRY_AGC)
tagNET_DVR_THERMOMETRY_AGC = struct_tagNET_DVR_THERMOMETRY_AGC
