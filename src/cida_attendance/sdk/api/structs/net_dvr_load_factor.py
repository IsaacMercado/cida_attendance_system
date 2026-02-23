from ctypes import Structure, c_int

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_LOAD_FACTOR(Structure):
    pass

_S(struct_tagNET_DVR_LOAD_FACTOR, [
    ('iPhaseALoadFactor', c_int),
    ('iPhaseBLoadFactor', c_int),
    ('iPhaseCLoadFactor', c_int),
    ('byRes', BYTE * 4),
])

NET_DVR_LOAD_FACTOR = struct_tagNET_DVR_LOAD_FACTOR
LPNET_DVR_LOAD_FACTOR = POINTER(struct_tagNET_DVR_LOAD_FACTOR)
tagNET_DVR_LOAD_FACTOR = struct_tagNET_DVR_LOAD_FACTOR
