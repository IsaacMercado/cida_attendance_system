from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_anon_38(Structure):
    pass

_S(struct_anon_38, [
    ('wAllDayRecord', WORD),
    ('byRecordType', BYTE),
    ('reservedData', c_char),
])

NET_DVR_RECORDDAY = struct_anon_38
LPNET_DVR_RECORDDAY = POINTER(struct_anon_38)
