from ctypes import Structure, c_int

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_FREQUENCY(Structure):
    pass

_S(struct_tagNET_DVR_FREQUENCY, [
    ('iPhaseAFrequency', c_int),
    ('iPhaseBFrequency', c_int),
    ('iPhaseCFrequency', c_int),
    ('byRes', BYTE * 4),
])

NET_DVR_FREQUENCY = struct_tagNET_DVR_FREQUENCY
LPNET_DVR_FREQUENCY = POINTER(struct_tagNET_DVR_FREQUENCY)
tagNET_DVR_FREQUENCY = struct_tagNET_DVR_FREQUENCY
