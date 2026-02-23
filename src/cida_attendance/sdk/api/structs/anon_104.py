from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .anon_101 import NET_DVR_USER_INFO_EX


class struct_anon_104(Structure):
    pass

_S(struct_anon_104, [
    ('dwSize', DWORD),
    ('struUser', NET_DVR_USER_INFO_EX * 16),
])

NET_DVR_USER_EX = struct_anon_104
LPNET_DVR_USER_EX = POINTER(struct_anon_104)
