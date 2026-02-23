from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_6 import NET_DVR_SCHEDTIME
from .anon_7 import NET_DVR_HANDLEEXCEPTION_V30


class struct_tagNet_DVR_ANALOG_ALARMINCFG(Structure):
    pass

_S(struct_tagNet_DVR_ANALOG_ALARMINCFG, [
    ('dwSize', DWORD),
    ('byEnableAlarmHandle', BYTE),
    ('byRes1', BYTE * 3),
    ('byAlarmInName', BYTE * 32),
    ('wAlarmInUpper', WORD),
    ('wAlarmInLower', WORD),
    ('struAlarmHandleType', NET_DVR_HANDLEEXCEPTION_V30),
    ('struAlarmTime', (NET_DVR_SCHEDTIME * 8) * 7),
    ('byRelRecordChan', BYTE * int((32 + 32))),
    ('byRes2', BYTE * 100),
])

NET_DVR_ANALOG_ALARMINCFG = struct_tagNet_DVR_ANALOG_ALARMINCFG
LPNET_DVR_ANALOG_ALARMINCFG = POINTER(struct_tagNet_DVR_ANALOG_ALARMINCFG)
tagNet_DVR_ANALOG_ALARMINCFG = struct_tagNet_DVR_ANALOG_ALARMINCFG
