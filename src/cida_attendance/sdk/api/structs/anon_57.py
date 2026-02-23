from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_6 import NET_DVR_SCHEDTIME
from .anon_7 import NET_DVR_HANDLEEXCEPTION_V30


class struct_anon_57(Structure):
    pass

_S(struct_anon_57, [
    ('dwSize', DWORD),
    ('sAlarmInName', BYTE * 32),
    ('byAlarmType', BYTE),
    ('byAlarmInHandle', BYTE),
    ('byChannel', BYTE),
    ('byInputType', BYTE),
    ('struAlarmHandleType', NET_DVR_HANDLEEXCEPTION_V30),
    ('struAlarmTime', (NET_DVR_SCHEDTIME * 8) * 7),
    ('byRelRecordChan', BYTE * int((32 + 32))),
    ('byEnablePreset', BYTE * int((32 + 32))),
    ('byPresetNo', BYTE * int((32 + 32))),
    ('byRes2', BYTE * 192),
    ('byEnableCruise', BYTE * int((32 + 32))),
    ('byCruiseNo', BYTE * int((32 + 32))),
    ('byEnablePtzTrack', BYTE * int((32 + 32))),
    ('byPTZTrack', BYTE * int((32 + 32))),
    ('byRes3', BYTE * 16),
])

NET_DVR_ALARMINCFG_V30 = struct_anon_57
LPNET_DVR_ALARMINCFG_V30 = POINTER(struct_anon_57)
