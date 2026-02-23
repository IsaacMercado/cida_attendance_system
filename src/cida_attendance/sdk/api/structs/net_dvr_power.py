from ctypes import Structure, c_int

from ..base_classes import _S
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_POWER(Structure):
    pass

_S(struct_tagNET_DVR_POWER, [
    ('iPhaseAPower', c_int),
    ('iPhaseBPower', c_int),
    ('iPhaseCPower', c_int),
    ('iSysTotalPower', c_int),
])

NET_DVR_POWER = struct_tagNET_DVR_POWER
LPNET_DVR_POWER = POINTER(struct_tagNET_DVR_POWER)
tagNET_DVR_POWER = struct_tagNET_DVR_POWER
