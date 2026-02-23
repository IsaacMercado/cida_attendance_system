from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_167 import NET_DVR_MATRIX_TRAN_CHAN_INFO


class struct_anon_168(Structure):
    pass

_S(struct_anon_168, [
    ('dwSize', DWORD),
    ('by232IsDualChan', BYTE),
    ('by485IsDualChan', BYTE),
    ('res', BYTE * 2),
    ('struTranInfo', NET_DVR_MATRIX_TRAN_CHAN_INFO * 64),
])

NET_DVR_MATRIX_TRAN_CHAN_CONFIG = struct_anon_168
LPNET_DVR_MATRIX_TRAN_CHAN_CONFIG = POINTER(struct_anon_168)
