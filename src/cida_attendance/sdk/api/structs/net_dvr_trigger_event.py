from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_TRIGGER_EVENT(Structure):
    pass

_S(struct_tagNET_DVR_TRIGGER_EVENT, [
    ('dwSize', DWORD),
    ('dwOverallEventTriggerAlarmoutOn', DWORD),
    ('dwOverallEventTriggerAlarmoutOff', DWORD),
    ('dwSubSystemEventTriggerAlarmoutOn', DWORD * 32),
    ('dwSubSystemEventTriggerAlarmoutOff', DWORD * 32),
    ('byRes', BYTE * 128),
])

NET_DVR_TRIGGER_EVENT = struct_tagNET_DVR_TRIGGER_EVENT
LPNET_DVR_TRIGGER_EVENT = POINTER(struct_tagNET_DVR_TRIGGER_EVENT)
tagNET_DVR_TRIGGER_EVENT = struct_tagNET_DVR_TRIGGER_EVENT
