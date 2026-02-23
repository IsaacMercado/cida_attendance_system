from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_stream_info import NET_DVR_STREAM_INFO


class struct_tagNET_DVR_ADD_RECORD_PASSBACK_MANUAL_COND(Structure):
    pass

_S(struct_tagNET_DVR_ADD_RECORD_PASSBACK_MANUAL_COND, [
    ('dwSize', DWORD),
    ('struStreamInfo', NET_DVR_STREAM_INFO),
    ('byRes', BYTE * 128),
])

NET_DVR_ADD_RECORD_PASSBACK_MANUAL_COND = struct_tagNET_DVR_ADD_RECORD_PASSBACK_MANUAL_COND
LPNET_DVR_ADD_RECORD_PASSBACK_MANUAL_COND = POINTER(struct_tagNET_DVR_ADD_RECORD_PASSBACK_MANUAL_COND)
tagNET_DVR_ADD_RECORD_PASSBACK_MANUAL_COND = struct_tagNET_DVR_ADD_RECORD_PASSBACK_MANUAL_COND
