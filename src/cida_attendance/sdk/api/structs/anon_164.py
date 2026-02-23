from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .anon_160 import NET_DVR_MATRIX_DECINFO


class struct_anon_164(Structure):
    pass

_S(struct_anon_164, [
    ('dwEnable', DWORD),
    ('struDecChanInfo', NET_DVR_MATRIX_DECINFO),
])

NET_DVR_MATRIX_DECCHANINFO = struct_anon_164
LPNET_DVR_MATRIX_DECCHANINFO = POINTER(struct_anon_164)
