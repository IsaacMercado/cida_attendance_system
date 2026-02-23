from ctypes import Structure, c_int

from ..base_classes import _S
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_VOLTAGE(Structure):
    pass

_S(struct_tagNET_DVR_VOLTAGE, [
    ('iPhaseAVol', c_int),
    ('iPhaseBVol', c_int),
    ('iPhaseCVol', c_int),
    ('iAveragePhaseVol', c_int),
])

NET_DVR_VOLTAGE = struct_tagNET_DVR_VOLTAGE
LPNET_DVR_VOLTAGE = POINTER(struct_tagNET_DVR_VOLTAGE)
tagNET_DVR_VOLTAGE = struct_tagNET_DVR_VOLTAGE
