from ctypes import Structure, c_int

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CURRENT(Structure):
    pass

_S(struct_tagNET_DVR_CURRENT, [
    ('iPhaseACurrent', c_int),
    ('iPhaseBCurrent', c_int),
    ('iPhaseCCurrent', c_int),
    ('byRes', BYTE * 4),
])

NET_DVR_CURRENT = struct_tagNET_DVR_CURRENT
LPNET_DVR_CURRENT = POINTER(struct_tagNET_DVR_CURRENT)
tagNET_DVR_CURRENT = struct_tagNET_DVR_CURRENT
