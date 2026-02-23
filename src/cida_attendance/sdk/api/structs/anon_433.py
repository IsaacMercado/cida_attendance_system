from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_432 import NET_DVR_CRUISEPOINT_PARAM


class struct_anon_433(Structure):
    pass

_S(struct_anon_433, [
    ('dwSize', DWORD),
    ('struCruisePoint', NET_DVR_CRUISEPOINT_PARAM * 128),
    ('Res', BYTE * 64),
])

NET_DVR_CRUISEPOINT_V40 = struct_anon_433
LPNET_DVR_CRUISEPOINT_V40 = POINTER(struct_anon_433)
