from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ALARMHOST_EXCEPTION_ALARM(Structure):
    pass

_S(struct_tagNET_DVR_ALARMHOST_EXCEPTION_ALARM, [
    ('dwSize', DWORD),
    ('dwExceptionType', DWORD),
    ('byRes', BYTE * 36),
])

NET_DVR_ALARMHOST_EXCEPTION_ALARM = struct_tagNET_DVR_ALARMHOST_EXCEPTION_ALARM
LPNET_DVR_ALARMHOST_EXCEPTION_ALARM = POINTER(struct_tagNET_DVR_ALARMHOST_EXCEPTION_ALARM)
tagNET_DVR_ALARMHOST_EXCEPTION_ALARM = struct_tagNET_DVR_ALARMHOST_EXCEPTION_ALARM
