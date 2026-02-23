from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_time_ex import NET_DVR_TIME_EX


class struct_tagNET_DVR_RECORD_CHECK_RET(Structure):
    pass

_S(struct_tagNET_DVR_RECORD_CHECK_RET, [
    ('dwSize', DWORD),
    ('byRecordNotComplete', BYTE),
    ('byRes1', BYTE * 3),
    ('struBeginTime', NET_DVR_TIME_EX),
    ('struEndTime', NET_DVR_TIME_EX),
    ('byRes', BYTE * 128),
])

NET_DVR_RECORD_CHECK_RET = struct_tagNET_DVR_RECORD_CHECK_RET
LPNET_DVR_RECORD_CHECK_RET = POINTER(struct_tagNET_DVR_RECORD_CHECK_RET)
tagNET_DVR_RECORD_CHECK_RET = struct_tagNET_DVR_RECORD_CHECK_RET
