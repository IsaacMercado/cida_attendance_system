from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER, String
from .anon_198 import NET_DVR_ALARMER


class struct_tagNET_DVR_ALARM_SEARCH_RESULT(Structure):
    pass

_S(struct_tagNET_DVR_ALARM_SEARCH_RESULT, [
    ('dwSize', DWORD),
    ('dwAlarmComm', DWORD),
    ('dwAlarmLen', DWORD),
    ('pAlarmInfo', String),
    ('struAlarmer', NET_DVR_ALARMER),
    ('byRes', BYTE * 128),
])

NET_DVR_ALARM_SEARCH_RESULT = struct_tagNET_DVR_ALARM_SEARCH_RESULT
LPNET_DVR_ALARM_SEARCH_RESULT = POINTER(struct_tagNET_DVR_ALARM_SEARCH_RESULT)
tagNET_DVR_ALARM_SEARCH_RESULT = struct_tagNET_DVR_ALARM_SEARCH_RESULT
