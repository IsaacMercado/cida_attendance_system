from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .anon_124 import NET_DVR_PORTINFO


class struct_anon_125(Structure):
    pass

_S(struct_anon_125, [
    ('dwSize', DWORD),
    ('struTransPortInfo', NET_DVR_PORTINFO * 2),
])

NET_DVR_PORTCFG = struct_anon_125
LPNET_DVR_PORTCFG = POINTER(struct_anon_125)
