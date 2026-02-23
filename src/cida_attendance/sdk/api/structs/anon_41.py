from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_anon_41(Structure):
    pass

_S(struct_anon_41, [
    ('byAllDayRecord', BYTE),
    ('byRecordType', BYTE),
    ('byRes', BYTE * 62),
])

NET_DVR_RECORDDAY_V40 = struct_anon_41
LPNET_DVR_RECORDDAY_V40 = POINTER(struct_anon_41)
