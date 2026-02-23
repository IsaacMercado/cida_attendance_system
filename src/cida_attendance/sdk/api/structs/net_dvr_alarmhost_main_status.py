from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ALARMHOST_MAIN_STATUS(Structure):
    pass

_S(struct_tagNET_DVR_ALARMHOST_MAIN_STATUS, [
    ('dwSize', DWORD),
    ('bySetupAlarmStatus', BYTE * 512),
    ('byAlarmInStatus', BYTE * 512),
    ('byAlarmOutStatus', BYTE * 512),
    ('byBypassStatus', BYTE * 512),
    ('bySubSystemGuardStatus', BYTE * 32),
    ('byAlarmInFaultStatus', BYTE * 512),
    ('byRes', BYTE * 56),
])

NET_DVR_ALARMHOST_MAIN_STATUS = struct_tagNET_DVR_ALARMHOST_MAIN_STATUS
LPNET_DVR_ALARMHOST_MAIN_STATUS = POINTER(struct_tagNET_DVR_ALARMHOST_MAIN_STATUS)
tagNET_DVR_ALARMHOST_MAIN_STATUS = struct_tagNET_DVR_ALARMHOST_MAIN_STATUS
