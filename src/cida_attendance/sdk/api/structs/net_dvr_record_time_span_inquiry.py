from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_RECORD_TIME_SPAN_INQUIRY(Structure):
    pass

_S(struct_tagNET_DVR_RECORD_TIME_SPAN_INQUIRY, [
    ('dwSize', DWORD),
    ('byType', BYTE),
    ('byRes', BYTE * 63),
])

NET_DVR_RECORD_TIME_SPAN_INQUIRY = struct_tagNET_DVR_RECORD_TIME_SPAN_INQUIRY
LPNET_DVR_RECORD_TIME_SPAN_INQUIRY = POINTER(struct_tagNET_DVR_RECORD_TIME_SPAN_INQUIRY)
tagNET_DVR_RECORD_TIME_SPAN_INQUIRY = struct_tagNET_DVR_RECORD_TIME_SPAN_INQUIRY
