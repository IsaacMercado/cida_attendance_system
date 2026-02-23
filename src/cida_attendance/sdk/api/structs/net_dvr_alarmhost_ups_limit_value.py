from ctypes import Structure, c_int

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ALARMHOST_UPS_LIMIT_VALUE(Structure):
    pass

_S(struct_tagNET_DVR_ALARMHOST_UPS_LIMIT_VALUE, [
    ('iInputVolHigh', c_int),
    ('iInputVolLow', c_int),
    ('iInputFreHigh', c_int),
    ('iInputFreLow', c_int),
    ('iOutputVolHigh', c_int),
    ('iOutputVolLow', c_int),
    ('iBatteryVoltageLow', c_int),
    ('iBatterySurplus', c_int),
    ('iBatteryTemperatureHigh', c_int),
    ('byRes', BYTE * 64),
])

NET_DVR_ALARMHOST_UPS_LIMIT_VALUE = struct_tagNET_DVR_ALARMHOST_UPS_LIMIT_VALUE
LPNET_DVR_ALARMHOST_UPS_LIMIT_VALUE = POINTER(struct_tagNET_DVR_ALARMHOST_UPS_LIMIT_VALUE)
tagNET_DVR_ALARMHOST_UPS_LIMIT_VALUE = struct_tagNET_DVR_ALARMHOST_UPS_LIMIT_VALUE
