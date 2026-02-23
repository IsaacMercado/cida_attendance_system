from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME


class struct_tagNET_DVR_ALARMINFO_DEV(Structure):
    pass

_S(struct_tagNET_DVR_ALARMINFO_DEV, [
    ('dwAlarmType', DWORD),
    ('struTime', NET_DVR_TIME),
    ('byRes', BYTE * 32),
    ('dwNumber', DWORD),
    ('pNO', POINTER(WORD)),
])

NET_DVR_ALARMINFO_DEV = struct_tagNET_DVR_ALARMINFO_DEV
LPNET_DVR_ALARMINFO_DEV = POINTER(struct_tagNET_DVR_ALARMINFO_DEV)
tagNET_DVR_ALARMINFO_DEV = struct_tagNET_DVR_ALARMINFO_DEV
