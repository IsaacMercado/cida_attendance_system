from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_69 import union_anon_69
from .net_dvr_time_ex import NET_DVR_TIME_EX


class struct_tagNET_DVR_ALARMINFO_FIXED_HEADER(Structure):
    pass

_S(struct_tagNET_DVR_ALARMINFO_FIXED_HEADER, [
    ('dwAlarmType', DWORD),
    ('struAlarmTime', NET_DVR_TIME_EX),
    ('uStruAlarm', union_anon_69),
    ('pRes', POINTER(DWORD)),
    ('byTimeDiffFlag', BYTE),
    ('cTimeDifferenceH', c_char),
    ('cTimeDifferenceM', c_char),
    ('byRes', BYTE),
    ('wDevInfoIvmsChannel', WORD),
    ('byRes2', BYTE * 2),
])

NET_DVR_ALRAM_FIXED_HEADER = struct_tagNET_DVR_ALARMINFO_FIXED_HEADER
LPNET_DVR_ALARM_FIXED_HEADER = POINTER(struct_tagNET_DVR_ALARMINFO_FIXED_HEADER)
tagNET_DVR_ALARMINFO_FIXED_HEADER = struct_tagNET_DVR_ALARMINFO_FIXED_HEADER
