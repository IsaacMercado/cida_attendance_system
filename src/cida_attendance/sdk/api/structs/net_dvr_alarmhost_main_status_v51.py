from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ALARMHOST_MAIN_STATUS_V51(Structure):
    pass

_S(struct_tagNET_DVR_ALARMHOST_MAIN_STATUS_V51, [
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
    ('bySubSystemAlarm', BYTE * 32),
    ('byAlarmOutCharge', BYTE * 512),
    ('byAlarmOutTamperStatus', BYTE * 512),
    ('byAlarmInShieldedStatus', BYTE * 512),
    ('byAlarmOutLinkage', BYTE * 512),
    ('byRes', BYTE * 512),
])

NET_DVR_ALARMHOST_MAIN_STATUS_V51 = struct_tagNET_DVR_ALARMHOST_MAIN_STATUS_V51
LPNET_DVR_ALARMHOST_MAIN_STATUS_V51 = POINTER(struct_tagNET_DVR_ALARMHOST_MAIN_STATUS_V51)
tagNET_DVR_ALARMHOST_MAIN_STATUS_V51 = struct_tagNET_DVR_ALARMHOST_MAIN_STATUS_V51
