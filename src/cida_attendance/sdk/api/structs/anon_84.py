from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .anon_83 import NET_DVR_SINGLE_HD


class struct_anon_84(Structure):
    pass

_S(struct_anon_84, [
    ('dwSize', DWORD),
    ('dwHDCount', DWORD),
    ('struHDInfo', NET_DVR_SINGLE_HD * 33),
])

NET_DVR_HDCFG = struct_anon_84
LPNET_DVR_HDCFG = POINTER(struct_anon_84)
