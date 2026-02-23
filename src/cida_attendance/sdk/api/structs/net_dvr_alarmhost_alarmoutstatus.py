from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ALARMHOST_ALARMOUTSTATUS(Structure):
    pass

_S(struct_tagNET_DVR_ALARMHOST_ALARMOUTSTATUS, [
    ('dwSize', DWORD),
    ('byName', BYTE * 32),
    ('byAlarmType', BYTE),
    ('wChan', WORD),
    ('byAlarmStatus', BYTE),
    ('byRes', BYTE * 32),
])

NET_DVR_ALARMHOST_ALARMOUTSTATUS = struct_tagNET_DVR_ALARMHOST_ALARMOUTSTATUS
LPNET_DVR_ALARMHOST_ALARMOUTSTATUS = POINTER(struct_tagNET_DVR_ALARMHOST_ALARMOUTSTATUS)
tagNET_DVR_ALARMHOST_ALARMOUTSTATUS = struct_tagNET_DVR_ALARMHOST_ALARMOUTSTATUS
