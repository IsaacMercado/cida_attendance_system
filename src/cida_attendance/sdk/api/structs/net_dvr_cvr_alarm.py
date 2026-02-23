from ctypes import Structure, c_char

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME


class struct_tagNET_DVR_CVR_ALARM(Structure):
    pass

_S(struct_tagNET_DVR_CVR_ALARM, [
    ('szFirstType', c_char * 32),
    ('szFirstIndex', c_char * 32),
    ('szSecondType', c_char * 32),
    ('struTime', NET_DVR_TIME),
    ('byStatus', BYTE),
    ('byAlarmLevel', BYTE),
    ('byRes1', BYTE * 2),
    ('szSecondIndex', c_char * 32),
    ('szThirdType', c_char * 32),
    ('szThirdIndex', c_char * 32),
    ('szFourthType', c_char * 32),
    ('szFourthIndex', c_char * 32),
    ('byRes2', BYTE * 92),
])

NET_DVR_CVR_ALARM = struct_tagNET_DVR_CVR_ALARM
LPNET_DVR_CVR_ALARM = POINTER(struct_tagNET_DVR_CVR_ALARM)
tagNET_DVR_CVR_ALARM = struct_tagNET_DVR_CVR_ALARM
