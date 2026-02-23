from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_RECORD_PASSBACK_TASK_CFG(Structure):
    pass

_S(struct_tagNET_DVR_RECORD_PASSBACK_TASK_CFG, [
    ('dwSize', DWORD),
    ('dwTaskID', DWORD),
    ('byRes', BYTE * 160),
])

NET_DVR_RECORD_PASSBACK_TASK_CFG = struct_tagNET_DVR_RECORD_PASSBACK_TASK_CFG
LPNET_DVR_RECORD_PASSBACK_TASK_CFG = POINTER(struct_tagNET_DVR_RECORD_PASSBACK_TASK_CFG)
tagNET_DVR_RECORD_PASSBACK_TASK_CFG = struct_tagNET_DVR_RECORD_PASSBACK_TASK_CFG
