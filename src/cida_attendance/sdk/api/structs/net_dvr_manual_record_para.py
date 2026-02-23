from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_stream_info import NET_DVR_STREAM_INFO


class struct_tagNET_DVR_MANUAL_RECORD_PARA(Structure):
    pass

_S(struct_tagNET_DVR_MANUAL_RECORD_PARA, [
    ('struStreamInfo', NET_DVR_STREAM_INFO),
    ('lRecordType', DWORD),
    ('byRes', BYTE * 32),
])

NET_DVR_MANUAL_RECORD_PARA = struct_tagNET_DVR_MANUAL_RECORD_PARA
LPNET_DVR_MANUAL_RECORD_PARA = POINTER(struct_tagNET_DVR_MANUAL_RECORD_PARA)
tagNET_DVR_MANUAL_RECORD_PARA = struct_tagNET_DVR_MANUAL_RECORD_PARA
