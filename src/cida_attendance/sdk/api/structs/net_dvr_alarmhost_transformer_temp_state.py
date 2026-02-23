from ctypes import Structure, c_int

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ALARMHOST_TRANSFORMER_TEMP_STATE(Structure):
    pass

_S(struct_tagNET_DVR_ALARMHOST_TRANSFORMER_TEMP_STATE, [
    ('iPhaseATemperature', c_int),
    ('iPhaseBTemperature', c_int),
    ('iPhaseCTemperature', c_int),
    ('iPhaseDTemperature', c_int),
    ('byRes', BYTE * 496),
])

NET_DVR_ALARMHOST_TRANSFORMER_TEMP_STATE = struct_tagNET_DVR_ALARMHOST_TRANSFORMER_TEMP_STATE
LPNET_DVR_ALARMHOST_TRANSFORMER_TEMP_STATE = POINTER(struct_tagNET_DVR_ALARMHOST_TRANSFORMER_TEMP_STATE)
tagNET_DVR_ALARMHOST_TRANSFORMER_TEMP_STATE = struct_tagNET_DVR_ALARMHOST_TRANSFORMER_TEMP_STATE
