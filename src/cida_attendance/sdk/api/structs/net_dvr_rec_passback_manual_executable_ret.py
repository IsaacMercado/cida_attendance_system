from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_stream_info import NET_DVR_STREAM_INFO


class struct_tagNET_DVR_REC_PASSBACK_MANUAL_EXECUTABLE_RET(Structure):
    pass

_S(struct_tagNET_DVR_REC_PASSBACK_MANUAL_EXECUTABLE_RET, [
    ('dwSize', DWORD),
    ('struStreamInfo', NET_DVR_STREAM_INFO),
    ('byExecutable', BYTE),
    ('byUnexecutableReason', BYTE),
    ('byRes', BYTE * 254),
])

NET_DVR_REC_PASSBACK_MANUAL_EXECUTABLE_RET = struct_tagNET_DVR_REC_PASSBACK_MANUAL_EXECUTABLE_RET
LPNET_DVR_REC_PASSBACK_MANUAL_EXECUTABLE_RET = POINTER(struct_tagNET_DVR_REC_PASSBACK_MANUAL_EXECUTABLE_RET)
tagNET_DVR_REC_PASSBACK_MANUAL_EXECUTABLE_RET = struct_tagNET_DVR_REC_PASSBACK_MANUAL_EXECUTABLE_RET
