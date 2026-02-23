from ctypes import Structure, c_char

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME


class struct_anon_204(Structure):
    pass

_S(struct_anon_204, [
    ('sFileName', c_char * 100),
    ('struStartTime', NET_DVR_TIME),
    ('struStopTime', NET_DVR_TIME),
    ('dwFileSize', DWORD),
    ('sCardNum', c_char * 32),
])

NET_DVR_FINDDATA_CARD = struct_anon_204
LPNET_DVR_FINDDATA_CARD = POINTER(struct_anon_204)
