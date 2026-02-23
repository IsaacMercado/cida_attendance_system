from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .anon_164 import NET_DVR_MATRIX_DECCHANINFO


class struct_anon_165(Structure):
    pass

_S(struct_anon_165, [
    ('dwSize', DWORD),
    ('dwPoolTime', DWORD),
    ('struchanConInfo', NET_DVR_MATRIX_DECCHANINFO * 16),
])

NET_DVR_MATRIX_LOOP_DECINFO = struct_anon_165
LPNET_DVR_MATRIX_LOOP_DECINFO = POINTER(struct_anon_165)
