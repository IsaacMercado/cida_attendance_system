from ctypes import Structure, c_int

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ALARMHOST_TEMP_HUMIDITY_SENSOR_LIMIT_VALUE(Structure):
    pass

_S(struct_tagNET_DVR_ALARMHOST_TEMP_HUMIDITY_SENSOR_LIMIT_VALUE, [
    ('iTemperatureHighLimit', c_int),
    ('iTemperatureLowLimit', c_int),
    ('iHumidityHighLimit', c_int),
    ('iHumidityLowLimit', c_int),
    ('byRes', BYTE * 84),
])

NET_DVR_ALARMHOST_TEMP_HUMIDITY_SENSOR_LIMIT_VALUE = struct_tagNET_DVR_ALARMHOST_TEMP_HUMIDITY_SENSOR_LIMIT_VALUE
LPNET_DVR_ALARMHOST_TEMP_HUMIDITY_SENSOR_LIMIT_VALUE = POINTER(struct_tagNET_DVR_ALARMHOST_TEMP_HUMIDITY_SENSOR_LIMIT_VALUE)
tagNET_DVR_ALARMHOST_TEMP_HUMIDITY_SENSOR_LIMIT_VALUE = struct_tagNET_DVR_ALARMHOST_TEMP_HUMIDITY_SENSOR_LIMIT_VALUE
