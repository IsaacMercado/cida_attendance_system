from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ALARMHOST_MAIN_STATUS_V40(Structure):
    pass

_S(struct_tagNET_DVR_ALARMHOST_MAIN_STATUS_V40, [
    ('dwSize', DWORD),
    ('bySetupAlarmStatus', BYTE * 512),
    ('byAlarmInStatus', BYTE * 512),
    ('byAlarmOutStatus', BYTE * 512),
    ('byBypassStatus', BYTE * 512),
    ('bySubSystemGuardStatus', BYTE * 32),
    ('byAlarmInFaultStatus', BYTE * 512),
    ('byAlarmInMemoryStatus', BYTE * 512),
    ('byAlarmInTamperStatus', BYTE * 512),
    ('byEnableSubSystem', BYTE * 32),
    ('bySubSystemGuardType', BYTE * 32),
    ('byRes', BYTE * 448),
])

NET_DVR_ALARMHOST_MAIN_STATUS_V40 = struct_tagNET_DVR_ALARMHOST_MAIN_STATUS_V40
LPNET_DVR_ALARMHOST_MAIN_STATUS_V40 = POINTER(struct_tagNET_DVR_ALARMHOST_MAIN_STATUS_V40)
tagNET_DVR_ALARMHOST_MAIN_STATUS_V40 = struct_tagNET_DVR_ALARMHOST_MAIN_STATUS_V40
