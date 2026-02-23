from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ALARMHOST_AUDIO_ASSOCIATE_ALARM(Structure):
    pass

_S(struct_tagNET_DVR_ALARMHOST_AUDIO_ASSOCIATE_ALARM, [
    ('dwSize', DWORD),
    ('byEnterDoor', BYTE * 8),
    ('byExitDoor', BYTE * 8),
    ('byAlarmIn', BYTE * 512),
    ('byRes', BYTE * 128),
])

NET_DVR_ALARMHOST_AUDIO_ASSOCIATE_ALARM = struct_tagNET_DVR_ALARMHOST_AUDIO_ASSOCIATE_ALARM
LPNET_DVR_ALARMHOST_AUDIO_ASSOCIATE_ALARM = POINTER(struct_tagNET_DVR_ALARMHOST_AUDIO_ASSOCIATE_ALARM)
tagNET_DVR_ALARMHOST_AUDIO_ASSOCIATE_ALARM = struct_tagNET_DVR_ALARMHOST_AUDIO_ASSOCIATE_ALARM
