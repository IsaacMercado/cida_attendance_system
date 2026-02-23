from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_7 import NET_DVR_HANDLEEXCEPTION_V30


class struct_tagNET_IPC_CALLHELP_ALARMCFG(Structure):
    pass

_S(struct_tagNET_IPC_CALLHELP_ALARMCFG, [
    ('byAlarmHandle', BYTE),
    ('byRes1', BYTE * 3),
    ('struAlarmHandleType', NET_DVR_HANDLEEXCEPTION_V30),
    ('byRelRecordChan', BYTE * int((32 + 32))),
    ('byRes', BYTE * 64),
])

NET_IPC_CALLHELP_ALARMCFG = struct_tagNET_IPC_CALLHELP_ALARMCFG
LPNET_IPC_CALLHELP_ALARMCFG = POINTER(struct_tagNET_IPC_CALLHELP_ALARMCFG)
tagNET_IPC_CALLHELP_ALARMCFG = struct_tagNET_IPC_CALLHELP_ALARMCFG
