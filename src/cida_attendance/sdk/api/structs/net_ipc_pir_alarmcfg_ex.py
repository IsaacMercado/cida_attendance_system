from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_6 import NET_DVR_SCHEDTIME
from .anon_7 import NET_DVR_HANDLEEXCEPTION_V30


class struct_tagNET_IPC_PIR_ALARMCFG_EX(Structure):
    pass

_S(struct_tagNET_IPC_PIR_ALARMCFG_EX, [
    ('byAlarmName', BYTE * 32),
    ('byAlarmHandle', BYTE),
    ('byRes1', BYTE * 3),
    ('struAlarmHandleType', NET_DVR_HANDLEEXCEPTION_V30),
    ('byRelRecordChan', BYTE * int((32 + 32))),
    ('struAlarmTime', (NET_DVR_SCHEDTIME * 8) * 7),
    ('byRes', BYTE * 1464),
])

NET_IPC_PIR_ALARMCFG_EX = struct_tagNET_IPC_PIR_ALARMCFG_EX
LPNET_IPC_PIR_ALARMCFG_EX = POINTER(struct_tagNET_IPC_PIR_ALARMCFG_EX)
tagNET_IPC_PIR_ALARMCFG_EX = struct_tagNET_IPC_PIR_ALARMCFG_EX
