from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ALARMHOST_SAFETYCABINSTATE(Structure):
    pass

_S(struct_tagNET_DVR_ALARMHOST_SAFETYCABINSTATE, [
    ('dwSize', DWORD),
    ('byEnterButton', BYTE),
    ('byExitButton', BYTE),
    ('byDoorState', BYTE),
    ('byLockState', BYTE),
    ('byUrgencyButton', BYTE),
    ('byManState', BYTE),
    ('byAbnormal', BYTE),
    ('byLightState', BYTE),
    ('byFanState', BYTE),
    ('byFollow', BYTE),
    ('byFighting', BYTE),
    ('byFaint', BYTE),
    ('byManyPerson', BYTE),
    ('byRes', BYTE * 59),
])

NET_DVR_ALARMHOST_SAFETYCABINSTATE = struct_tagNET_DVR_ALARMHOST_SAFETYCABINSTATE
LPNET_DVR_ALARMHOST_SAFETYCABINSTATE = POINTER(struct_tagNET_DVR_ALARMHOST_SAFETYCABINSTATE)
tagNET_DVR_ALARMHOST_SAFETYCABINSTATE = struct_tagNET_DVR_ALARMHOST_SAFETYCABINSTATE
