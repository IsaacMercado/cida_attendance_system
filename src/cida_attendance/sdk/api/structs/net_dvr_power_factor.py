from ctypes import Structure, c_int

from ..base_classes import _S
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_POWER_FACTOR(Structure):
    pass

_S(struct_tagNET_DVR_POWER_FACTOR, [
    ('iPhaseAPowerFactor', c_int),
    ('iPhaseBPowerFactor', c_int),
    ('iPhaseCPowerFactor', c_int),
    ('iTotalPowerFactor', c_int),
])

NET_DVR_POWER_FACTOR = struct_tagNET_DVR_POWER_FACTOR
LPNET_DVR_POWER_FACTOR = POINTER(struct_tagNET_DVR_POWER_FACTOR)
tagNET_DVR_POWER_FACTOR = struct_tagNET_DVR_POWER_FACTOR
