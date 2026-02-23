from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_37 import NET_DVR_RECORDSCHED
from .anon_38 import NET_DVR_RECORDDAY


class struct_tagNET_DVR_HOLIDAY_RECORD(Structure):
    pass

_S(struct_tagNET_DVR_HOLIDAY_RECORD, [
    ('dwSize', DWORD),
    ('struRecDay', NET_DVR_RECORDDAY),
    ('struRecordSched', NET_DVR_RECORDSCHED * 8),
    ('byRes', BYTE * 20),
])

NET_DVR_HOLIDAY_RECORD = struct_tagNET_DVR_HOLIDAY_RECORD
LPNET_DVR_HOLIDAY_RECORD = POINTER(struct_tagNET_DVR_HOLIDAY_RECORD)
tagNET_DVR_HOLIDAY_RECORD = struct_tagNET_DVR_HOLIDAY_RECORD
