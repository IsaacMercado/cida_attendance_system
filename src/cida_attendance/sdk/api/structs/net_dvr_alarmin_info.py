from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_stream_info import NET_DVR_STREAM_INFO


class struct_tagNET_DVR_ALARMIN_INFO(Structure):
    pass

_S(struct_tagNET_DVR_ALARMIN_INFO, [
    ('struStreamInfo', NET_DVR_STREAM_INFO),
    ('dwAlarmInChannel', DWORD),
    ('byRes', BYTE * 32),
])

NET_DVR_ALARMIN_INFO = struct_tagNET_DVR_ALARMIN_INFO
LPNET_DVR_ALARMIN_INFO = POINTER(struct_tagNET_DVR_ALARMIN_INFO)
tagNET_DVR_ALARMIN_INFO = struct_tagNET_DVR_ALARMIN_INFO
