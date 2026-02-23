from ctypes import Structure, c_int

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ALARMHOST_UPS_ALARMINFO(Structure):
    pass

_S(struct_tagNET_DVR_ALARMHOST_UPS_ALARMINFO, [
    ('byAlarmType', BYTE),
    ('byChanNo', BYTE),
    ('bySlotNo', BYTE),
    ('byRes1', BYTE),
    ('iAlarmValue', c_int),
    ('byRes2', BYTE * 64),
])

NET_DVR_ALARMHOST_UPS_ALARMINFO = struct_tagNET_DVR_ALARMHOST_UPS_ALARMINFO
LPNET_DVR_ALARMHOST_UPS_ALARMINFO = POINTER(struct_tagNET_DVR_ALARMHOST_UPS_ALARMINFO)
tagNET_DVR_ALARMHOST_UPS_ALARMINFO = struct_tagNET_DVR_ALARMHOST_UPS_ALARMINFO
