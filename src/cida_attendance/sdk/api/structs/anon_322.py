from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_anon_322(Structure):
    pass

_S(struct_anon_322, [
    ('struIP', NET_DVR_IPADDR),
    ('byRes', BYTE * 128),
])

NET_DVR_POE_CFG = struct_anon_322
LPNET_DVR_POE_CFG = POINTER(struct_anon_322)
