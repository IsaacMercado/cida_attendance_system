from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_7 import NET_DVR_HANDLEEXCEPTION_V30


class struct_tagNET_IPC_SINGLE_WIRELESS_ALARMCFG(Structure):
    pass

_S(struct_tagNET_IPC_SINGLE_WIRELESS_ALARMCFG, [
    ('byAlarmName', BYTE * 32),
    ('byAlarmHandle', BYTE),
    ('byID', BYTE),
    ('byRes1', BYTE * 2),
    ('struAlarmHandleType', NET_DVR_HANDLEEXCEPTION_V30),
    ('byRelRecordChan', BYTE * int((32 + 32))),
    ('byRes', BYTE * 32),
])

NET_IPC_SINGLE_WIRELESS_ALARMCFG = struct_tagNET_IPC_SINGLE_WIRELESS_ALARMCFG
LPNET_IPC_SINGLE_WIRELESS_ALARMCFG = POINTER(struct_tagNET_IPC_SINGLE_WIRELESS_ALARMCFG)
tagNET_IPC_SINGLE_WIRELESS_ALARMCFG = struct_tagNET_IPC_SINGLE_WIRELESS_ALARMCFG
