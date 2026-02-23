from ctypes import Structure, c_char

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_6 import NET_DVR_SCHEDTIME


class struct_anon_37(Structure):
    pass

_S(struct_anon_37, [
    ('struRecordTime', NET_DVR_SCHEDTIME),
    ('byRecordType', BYTE),
    ('reservedData', c_char * 3),
])

NET_DVR_RECORDSCHED = struct_anon_37
LPNET_DVR_RECORDSCHED = POINTER(struct_anon_37)
