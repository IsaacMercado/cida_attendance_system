from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_sensor_value import NET_DVR_SENSOR_VALUE
from .net_dvr_time_v30 import NET_DVR_TIME_V30


class struct_tagNET_DVR_HISTORICAL_QUERY_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_HISTORICAL_QUERY_PARAM, [
    ('struStartTime', NET_DVR_TIME_V30),
    ('struEndTime', NET_DVR_TIME_V30),
    ('struVoltageValue', NET_DVR_SENSOR_VALUE),
    ('struCurrentValue', NET_DVR_SENSOR_VALUE),
    ('struTemperatureValue', NET_DVR_SENSOR_VALUE),
    ('struHumidityValue', NET_DVR_SENSOR_VALUE),
    ('bySwitchStatus', BYTE),
    ('bySensorStatus', BYTE),
    ('byRes', BYTE * 66),
])

NET_DVR_HISTORICAL_QUERY_PARAM = struct_tagNET_DVR_HISTORICAL_QUERY_PARAM
LPNET_DVR_HISTORICAL_QUERY_PARAM = POINTER(struct_tagNET_DVR_HISTORICAL_QUERY_PARAM)
tagNET_DVR_HISTORICAL_QUERY_PARAM = struct_tagNET_DVR_HISTORICAL_QUERY_PARAM
