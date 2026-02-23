from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_6 import NET_DVR_SCHEDTIME


class struct_anon_40(Structure):
    pass

_S(struct_anon_40, [
    ('struRecordTime', NET_DVR_SCHEDTIME),
    ('byRecordType', BYTE),
    ('byRes', BYTE * 31),
])

NET_DVR_RECORDSCHED_V40 = struct_anon_40
LPNET_DVR_RECORDSCHED_V40 = POINTER(struct_anon_40)
