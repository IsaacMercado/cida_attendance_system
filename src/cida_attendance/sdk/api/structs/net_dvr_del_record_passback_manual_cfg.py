from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_stream_info import NET_DVR_STREAM_INFO


class struct_tagNET_DVR_DEL_RECORD_PASSBACK_MANUAL_CFG(Structure):
    pass

_S(struct_tagNET_DVR_DEL_RECORD_PASSBACK_MANUAL_CFG, [
    ('dwSize', DWORD),
    ('dwTaskID', DWORD),
    ('struStreamInfo', NET_DVR_STREAM_INFO),
    ('byRes', BYTE * 128),
])

NET_DVR_DEL_RECORD_PASSBACK_MANUAL_CFG = struct_tagNET_DVR_DEL_RECORD_PASSBACK_MANUAL_CFG
LPNET_DVR_DEL_RECORD_PASSBACK_MANUAL_CFG = POINTER(struct_tagNET_DVR_DEL_RECORD_PASSBACK_MANUAL_CFG)
tagNET_DVR_DEL_RECORD_PASSBACK_MANUAL_CFG = struct_tagNET_DVR_DEL_RECORD_PASSBACK_MANUAL_CFG
