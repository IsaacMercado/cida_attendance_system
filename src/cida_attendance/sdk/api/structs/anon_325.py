from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_324 import NET_DVR_MATRIX_CHAN_INFO_EX


class struct_anon_325(Structure):
    pass

_S(struct_anon_325, [
    ('dwSize', DWORD),
    ('dwPoolTime', DWORD),
    ('struchanConInfo', NET_DVR_MATRIX_CHAN_INFO_EX * 64),
    ('byRes', BYTE * 16),
])

NET_DVR_MATRIX_LOOP_DECINFO_EX = struct_anon_325
LPNET_DVR_MATRIX_LOOP_DECINFO_EX = POINTER(struct_anon_325)
