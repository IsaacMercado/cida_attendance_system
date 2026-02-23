from ctypes import Structure

from ..base_classes import _S, BYTE, LONG
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ALARMHOST_DUSTNOISE_SENSOR(Structure):
    pass

_S(struct_tagNET_DVR_ALARMHOST_DUSTNOISE_SENSOR, [
    ('iDust', LONG),
    ('iNoise', LONG),
    ('iPM25', LONG),
    ('byRes', BYTE * 500),
])

NET_DVR_ALARMHOST_DUSTNOISE_SENSOR = struct_tagNET_DVR_ALARMHOST_DUSTNOISE_SENSOR
LPNET_DVR_ALARMHOST_DUSTNOISE_SENSOR = POINTER(struct_tagNET_DVR_ALARMHOST_DUSTNOISE_SENSOR)
tagNET_DVR_ALARMHOST_DUSTNOISE_SENSOR = struct_tagNET_DVR_ALARMHOST_DUSTNOISE_SENSOR
