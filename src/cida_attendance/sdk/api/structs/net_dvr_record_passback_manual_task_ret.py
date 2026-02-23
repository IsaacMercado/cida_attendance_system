from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_stream_info import NET_DVR_STREAM_INFO
from .net_dvr_time_ex import NET_DVR_TIME_EX


class struct_tagNET_DVR_RECORD_PASSBACK_MANUAL_TASK_RET(Structure):
    pass

_S(struct_tagNET_DVR_RECORD_PASSBACK_MANUAL_TASK_RET, [
    ('dwSize', DWORD),
    ('struStreamInfo', NET_DVR_STREAM_INFO),
    ('dwTaskID', DWORD),
    ('struStartTime', NET_DVR_TIME_EX),
    ('struStopTime', NET_DVR_TIME_EX),
    ('byTaskStatus', BYTE),
    ('byRes1', BYTE * 3),
    ('struExecuteStartTime', NET_DVR_TIME_EX),
    ('struExecuteStopTime', NET_DVR_TIME_EX),
    ('byRes', BYTE * 128),
])

NET_DVR_RECORD_PASSBACK_MANUAL_TASK_RET = struct_tagNET_DVR_RECORD_PASSBACK_MANUAL_TASK_RET
LPNET_DVR_RECORD_PASSBACK_MANUAL_TASK_RET = POINTER(struct_tagNET_DVR_RECORD_PASSBACK_MANUAL_TASK_RET)
tagNET_DVR_RECORD_PASSBACK_MANUAL_TASK_RET = struct_tagNET_DVR_RECORD_PASSBACK_MANUAL_TASK_RET
