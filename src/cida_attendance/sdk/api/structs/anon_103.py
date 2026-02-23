from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .anon_100 import NET_DVR_USER_INFO_V30


class struct_anon_103(Structure):
    pass

_S(struct_anon_103, [
    ('dwSize', DWORD),
    ('struUser', NET_DVR_USER_INFO_V30 * 32),
])

NET_DVR_USER_V30 = struct_anon_103
LPNET_DVR_USER_V30 = POINTER(struct_anon_103)
