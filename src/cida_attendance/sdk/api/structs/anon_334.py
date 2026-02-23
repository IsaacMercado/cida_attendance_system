from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .anon_39 import NET_DVR_RECORD_V30


class struct_anon_334(Structure):
    pass

_S(struct_anon_334, [
    ('dwSize', DWORD),
    ('struRecordInfo', NET_DVR_RECORD_V30),
])

NET_DVR_STREAM_RECORD_INFO = struct_anon_334
LPNET_DVR_STREAM_RECORD_INFO = POINTER(struct_anon_334)
