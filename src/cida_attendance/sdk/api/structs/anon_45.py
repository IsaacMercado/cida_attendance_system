from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_44 import NET_DVR_PTZ_PROTOCOL


class struct_anon_45(Structure):
    pass

_S(struct_anon_45, [
    ('dwSize', DWORD),
    ('struPtz', NET_DVR_PTZ_PROTOCOL * 200),
    ('dwPtzNum', DWORD),
    ('byRes', BYTE * 8),
])

NET_DVR_PTZCFG = struct_anon_45
LPNET_DVR_PTZCFG = POINTER(struct_anon_45)
