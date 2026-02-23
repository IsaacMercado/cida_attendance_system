from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .anon_133 import NET_DVR_DECCHANSTATUS


class struct_anon_134(Structure):
    pass

_S(struct_anon_134, [
    ('dwSize', DWORD),
    ('struDecState', NET_DVR_DECCHANSTATUS * 4),
])

NET_DVR_DECSTATUS = struct_anon_134
LPNET_DVR_DECSTATUS = POINTER(struct_anon_134)
