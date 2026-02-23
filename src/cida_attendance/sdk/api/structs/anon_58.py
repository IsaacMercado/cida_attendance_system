from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_6 import NET_DVR_SCHEDTIME
from .anon_8 import NET_DVR_HANDLEEXCEPTION


class struct_anon_58(Structure):
    pass

_S(struct_anon_58, [
    ('dwSize', DWORD),
    ('sAlarmInName', BYTE * 32),
    ('byAlarmType', BYTE),
    ('byAlarmInHandle', BYTE),
    ('byChannel', BYTE),
    ('byRes', BYTE),
    ('struAlarmHandleType', NET_DVR_HANDLEEXCEPTION),
    ('struAlarmTime', (NET_DVR_SCHEDTIME * 4) * 7),
    ('byRelRecordChan', BYTE * 16),
    ('byEnablePreset', BYTE * 16),
    ('byPresetNo', BYTE * 16),
    ('byEnableCruise', BYTE * 16),
    ('byCruiseNo', BYTE * 16),
    ('byEnablePtzTrack', BYTE * 16),
    ('byPTZTrack', BYTE * 16),
])

NET_DVR_ALARMINCFG = struct_anon_58
LPNET_DVR_ALARMINCFG = POINTER(struct_anon_58)
