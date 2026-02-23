from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_447 import NET_DVR_RING_PORT_PROPERTY


class struct_anon_448(Structure):
    pass

_S(struct_anon_448, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byProtoType', BYTE),
    ('byBandWidth', BYTE),
    ('byRes1', BYTE),
    ('struRingPort', NET_DVR_RING_PORT_PROPERTY * 2),
    ('byRes2', BYTE * 60),
])

NET_DVR_NS_RING_CFG = struct_anon_448
LPNET_DVR_NS_RING_CFG = POINTER(struct_anon_448)
