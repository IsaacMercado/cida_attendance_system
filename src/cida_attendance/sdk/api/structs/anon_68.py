from ctypes import Structure

from ..base_classes import _S, BYTE
from .net_dvr_time_ex import NET_DVR_TIME_EX


class struct_anon_68(Structure):
    pass

_S(struct_anon_68, [
    ('struAlarmTime', NET_DVR_TIME_EX),
    ('byExceptionType', BYTE),
    ('byRes1', BYTE * 3),
])

