from ctypes import Structure, c_int

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ALARMHOST_TEMP_HUMI_SENSOR_STATE(Structure):
    pass

_S(struct_tagNET_DVR_ALARMHOST_TEMP_HUMI_SENSOR_STATE, [
    ('iTemperature', c_int),
    ('iHumidity', c_int),
    ('byRes', BYTE * 504),
])

NET_DVR_ALARMHOST_TEMP_HUMI_SENSOR_STATE = struct_tagNET_DVR_ALARMHOST_TEMP_HUMI_SENSOR_STATE
LPNET_DVR_ALARMHOST_TEMP_HUMI_SENSOR_STATE = POINTER(struct_tagNET_DVR_ALARMHOST_TEMP_HUMI_SENSOR_STATE)
tagNET_DVR_ALARMHOST_TEMP_HUMI_SENSOR_STATE = struct_tagNET_DVR_ALARMHOST_TEMP_HUMI_SENSOR_STATE
