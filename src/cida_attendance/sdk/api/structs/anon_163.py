from ctypes import Structure, c_char

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME
from .anon_160 import NET_DVR_MATRIX_DECINFO


class struct_anon_163(Structure):
    pass

_S(struct_anon_163, [
    ('dwSize', DWORD),
    ('struDecChanInfo', NET_DVR_MATRIX_DECINFO),
    ('dwDecState', DWORD),
    ('StartTime', NET_DVR_TIME),
    ('StopTime', NET_DVR_TIME),
    ('sFileName', c_char * 128),
])

NET_DVR_MATRIX_DEC_CHAN_INFO = struct_anon_163
LPNET_DVR_MATRIX_DEC_CHAN_INFO = POINTER(struct_anon_163)
