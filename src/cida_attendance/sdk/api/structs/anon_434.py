from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_432 import NET_DVR_CRUISEPOINT_PARAM


class struct_anon_434(Structure):
    pass

_S(struct_anon_434, [
    ('dwSize', DWORD),
    ('struCruisePoint', NET_DVR_CRUISEPOINT_PARAM * 256),
    ('Res', BYTE * 64),
])

NET_DVR_CRUISEPOINT_V50 = struct_anon_434
LPNET_DVR_CRUISEPOINT_V50 = POINTER(struct_anon_434)
