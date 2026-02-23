from ctypes import Structure, c_float

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_time_v30 import NET_DVR_TIME_V30


class struct_tagNET_DVR_SENSOR_CFG(Structure):
    pass

_S(struct_tagNET_DVR_SENSOR_CFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byDeviceType', BYTE),
    ('byDeviceID', BYTE),
    ('byRes1', BYTE),
    ('struTime', NET_DVR_TIME_V30),
    ('byIsFirst', BYTE),
    ('byIsSwitchOn', BYTE),
    ('bySensorStatus', BYTE),
    ('bySensorType', BYTE),
    ('fVoltage', c_float),
    ('fCurrent', c_float),
    ('fTemperatureValue', c_float),
    ('fHumidityValue', c_float),
    ('bySensorName', BYTE * 32),
    ('byDescription', BYTE * 64),
    ('fActualValue', c_float),
    ('byUnit', BYTE * 32),
    ('byRes', BYTE * 220),
])

NET_DVR_SENSOR_CFG = struct_tagNET_DVR_SENSOR_CFG
LPNET_DVR_SENSOR_CFG = POINTER(struct_tagNET_DVR_SENSOR_CFG)
tagNET_DVR_SENSOR_CFG = struct_tagNET_DVR_SENSOR_CFG
