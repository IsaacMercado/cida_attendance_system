from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_410 import NET_DVR_SCHEDTASK


class struct_tagNET_DVR_TIME_TASK(Structure):
    pass

_S(struct_tagNET_DVR_TIME_TASK, [
    ('dwSize', DWORD),
    ('byTaskEnable', BYTE),
    ('byRes', BYTE * 3),
    ('struTask', (NET_DVR_SCHEDTASK * 10) * 7),
    ('dwParkTime', DWORD),
    ('byRes1', BYTE * 64),
])

NET_DVR_TIME_TASK = struct_tagNET_DVR_TIME_TASK
LPNET_DVR_TIME_TASK = POINTER(struct_tagNET_DVR_TIME_TASK)
tagNET_DVR_TIME_TASK = struct_tagNET_DVR_TIME_TASK
