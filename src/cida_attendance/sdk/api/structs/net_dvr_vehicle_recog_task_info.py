from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_time_v30 import NET_DVR_TIME_V30


class struct_tagNET_DVR_VEHICLE_RECOG_TASK_INFO(Structure):
    pass

_S(struct_tagNET_DVR_VEHICLE_RECOG_TASK_INFO, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('sDataIndex', c_char * 64),
    ('wTaskNo', WORD),
    ('wTaskProgress', WORD),
    ('byTaskState', BYTE),
    ('byRes1', BYTE * 3),
    ('dwRecogOperate', DWORD),
    ('dwPostID', DWORD),
    ('struPostTime', NET_DVR_TIME_V30),
    ('dwJsonLen', DWORD),
    ('pJsonBuffer', POINTER(BYTE)),
    ('byRes', BYTE * 104),
])

NET_DVR_VEHICLE_RECOG_TASK_INFO = struct_tagNET_DVR_VEHICLE_RECOG_TASK_INFO
LPNET_DVR_VEHICLE_RECOG_TASK_INFO = POINTER(struct_tagNET_DVR_VEHICLE_RECOG_TASK_INFO)
tagNET_DVR_VEHICLE_RECOG_TASK_INFO = struct_tagNET_DVR_VEHICLE_RECOG_TASK_INFO
