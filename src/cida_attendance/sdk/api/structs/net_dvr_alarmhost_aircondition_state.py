from ctypes import Structure, c_int

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ALARMHOST_AIRCONDITION_STATE(Structure):
    pass

_S(struct_tagNET_DVR_ALARMHOST_AIRCONDITION_STATE, [
    ('iTemperature', c_int),
    ('iHumidity', c_int),
    ('byRunState', BYTE),
    ('byRes', BYTE * 503),
])

NET_DVR_ALARMHOST_AIRCONDITION_STATE = struct_tagNET_DVR_ALARMHOST_AIRCONDITION_STATE
LPNET_DVR_ALARMHOST_AIRCONDITION_STATE = POINTER(struct_tagNET_DVR_ALARMHOST_AIRCONDITION_STATE)
tagNET_DVR_ALARMHOST_AIRCONDITION_STATE = struct_tagNET_DVR_ALARMHOST_AIRCONDITION_STATE
