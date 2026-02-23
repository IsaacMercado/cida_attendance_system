from ctypes import Structure

from ..base_classes import _S
from ..ctypes_preamble import POINTER
from .anon_157 import NET_DVR_CRUISE_POINT


class struct_anon_158(Structure):
    pass

_S(struct_anon_158, [
    ('struCruisePoint', NET_DVR_CRUISE_POINT * 32),
])

NET_DVR_CRUISE_RET = struct_anon_158
LPNET_DVR_CRUISE_RET = POINTER(struct_anon_158)
