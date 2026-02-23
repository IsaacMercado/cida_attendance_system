from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .anon_160 import NET_DVR_MATRIX_DECINFO


class struct_anon_161(Structure):
    pass

_S(struct_anon_161, [
    ('dwSize', DWORD),
    ('struDecChanInfo', NET_DVR_MATRIX_DECINFO),
])

NET_DVR_MATRIX_DYNAMIC_DEC = struct_anon_161
LPNET_DVR_MATRIX_DYNAMIC_DEC = POINTER(struct_anon_161)
