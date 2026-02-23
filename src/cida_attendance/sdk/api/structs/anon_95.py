from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_anon_95(Structure):
    pass

_S(struct_anon_95, [
    ('wOrder', WORD * 32),
    ('wSwitchTime', WORD),
    ('res', BYTE * 14),
])

NET_DVR_MATRIXPARA_V30 = struct_anon_95
LPNET_DVR_MATRIXPARA_V30 = POINTER(struct_anon_95)
