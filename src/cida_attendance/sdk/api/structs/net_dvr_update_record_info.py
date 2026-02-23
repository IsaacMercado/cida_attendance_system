from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_stream_info import NET_DVR_STREAM_INFO


class struct_tagNET_DVR_UPDATE_RECORD_INFO(Structure):
    pass

_S(struct_tagNET_DVR_UPDATE_RECORD_INFO, [
    ('dwSize', DWORD),
    ('struStreasmInfo', NET_DVR_STREAM_INFO),
    ('dwBeginTime', DWORD),
    ('dwEndTime', DWORD),
    ('byRes', BYTE * 32),
])

NET_DVR_UPDATE_RECORD_INFO = struct_tagNET_DVR_UPDATE_RECORD_INFO
LPNET_DVR_UPDATE_RECORD_INFO = POINTER(struct_tagNET_DVR_UPDATE_RECORD_INFO)
tagNET_DVR_UPDATE_RECORD_INFO = struct_tagNET_DVR_UPDATE_RECORD_INFO
