from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_143 import NET_DVR_TIMEPOINT


class struct_anon_144(Structure):
    pass

_S(struct_anon_144, [
    ('dwSize', DWORD),
    ('dwZoneIndex', DWORD),
    ('byRes1', BYTE * 12),
    ('dwEnableDST', DWORD),
    ('byDSTBias', BYTE),
    ('byRes2', BYTE * 3),
    ('struBeginPoint', NET_DVR_TIMEPOINT),
    ('struEndPoint', NET_DVR_TIMEPOINT),
])

NET_DVR_ZONEANDDST = struct_anon_144
LPNET_DVR_ZONEANDDST = POINTER(struct_anon_144)
