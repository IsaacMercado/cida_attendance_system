from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_FIRE_ALARM_STATUS(Structure):
    pass

_S(struct_tagNET_DVR_FIRE_ALARM_STATUS, [
    ('byFireAlarm', (BYTE * 32) * 12),
    ('byRes', BYTE * 128),
])

NET_DVR_FIRE_ALARM_STATUS = struct_tagNET_DVR_FIRE_ALARM_STATUS
LPNET_DVR_FIRE_ALARM_STATUS = POINTER(struct_tagNET_DVR_FIRE_ALARM_STATUS)
tagNET_DVR_FIRE_ALARM_STATUS = struct_tagNET_DVR_FIRE_ALARM_STATUS
