from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .anon_37 import NET_DVR_RECORDSCHED
from .anon_38 import NET_DVR_RECORDDAY


class struct_anon_43(Structure):
    pass

_S(struct_anon_43, [
    ('dwSize', DWORD),
    ('dwRecord', DWORD),
    ('struRecAllDay', NET_DVR_RECORDDAY * 7),
    ('struRecordSched', (NET_DVR_RECORDSCHED * 4) * 7),
    ('dwRecordTime', DWORD),
    ('dwPreRecordTime', DWORD),
])

NET_DVR_RECORD = struct_anon_43
LPNET_DVR_RECORD = POINTER(struct_anon_43)
