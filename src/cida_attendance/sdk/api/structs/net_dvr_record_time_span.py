from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME


class struct_tagNET_DVR_RECORD_TIME_SPAN(Structure):
    pass

_S(struct_tagNET_DVR_RECORD_TIME_SPAN, [
    ('dwSize', DWORD),
    ('strBeginTime', NET_DVR_TIME),
    ('strEndTime', NET_DVR_TIME),
    ('byType', BYTE),
    ('byRes', BYTE * 35),
])

NET_DVR_RECORD_TIME_SPAN = struct_tagNET_DVR_RECORD_TIME_SPAN
LPNET_DVR_RECORD_TIME_SPAN = POINTER(struct_tagNET_DVR_RECORD_TIME_SPAN)
tagNET_DVR_RECORD_TIME_SPAN = struct_tagNET_DVR_RECORD_TIME_SPAN
