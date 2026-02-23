from ctypes import Structure, c_int

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SCREEN_WORK_STATE(Structure):
    pass

_S(struct_tagNET_DVR_SCREEN_WORK_STATE, [
    ('dwSize', DWORD),
    ('byFanStatus', BYTE),
    ('byFanExceptionStatus', BYTE),
    ('byRes1', BYTE * 2),
    ('dwWorkingHours', DWORD),
    ('byVersion', BYTE * 32),
    ('iTemperature', c_int),
    ('byTempState', BYTE),
    ('byRes', BYTE * 31),
])

NET_DVR_SCREEN_WORK_STATE = struct_tagNET_DVR_SCREEN_WORK_STATE
LPNET_DVR_SCREEN_WORK_STATE = POINTER(struct_tagNET_DVR_SCREEN_WORK_STATE)
tagNET_DVR_SCREEN_WORK_STATE = struct_tagNET_DVR_SCREEN_WORK_STATE
