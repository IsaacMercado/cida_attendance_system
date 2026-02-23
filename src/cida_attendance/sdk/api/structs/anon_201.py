from ctypes import Structure, c_char

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME


class struct_anon_201(Structure):
    pass

_S(struct_anon_201, [
    ('sFileName', c_char * 100),
    ('struStartTime', NET_DVR_TIME),
    ('struStopTime', NET_DVR_TIME),
    ('dwFileSize', DWORD),
])

NET_DVR_FIND_DATA = struct_anon_201
LPNET_DVR_FIND_DATA = POINTER(struct_anon_201)
