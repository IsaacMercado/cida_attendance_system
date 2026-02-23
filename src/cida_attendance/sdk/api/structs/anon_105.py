from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .anon_102 import NET_DVR_USER_INFO


class struct_anon_105(Structure):
    pass

_S(struct_anon_105, [
    ('dwSize', DWORD),
    ('struUser', NET_DVR_USER_INFO * 16),
])

NET_DVR_USER = struct_anon_105
LPNET_DVR_USER = POINTER(struct_anon_105)
