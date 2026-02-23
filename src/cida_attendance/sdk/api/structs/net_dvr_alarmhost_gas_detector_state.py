from ctypes import Structure, c_int

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ALARMHOST_GAS_DETECTOR_STATE(Structure):
    pass

_S(struct_tagNET_DVR_ALARMHOST_GAS_DETECTOR_STATE, [
    ('iSF6', c_int),
    ('iFlow', c_int),
    ('iTemperature', c_int),
    ('iO2', c_int),
    ('iHumidity', c_int),
    ('byRes', BYTE * 492),
])

NET_DVR_ALARMHOST_GAS_DETECTOR_STATE = struct_tagNET_DVR_ALARMHOST_GAS_DETECTOR_STATE
LPNET_DVR_ALARMHOST_GAS_DETECTOR_STATE = POINTER(struct_tagNET_DVR_ALARMHOST_GAS_DETECTOR_STATE)
tagNET_DVR_ALARMHOST_GAS_DETECTOR_STATE = struct_tagNET_DVR_ALARMHOST_GAS_DETECTOR_STATE
