from ctypes import Structure, c_char, c_float

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_time_v30 import NET_DVR_TIME_V30


class struct_tagNET_DVR_SENSOR_INFO_UPLOAD(Structure):
    pass

_S(struct_tagNET_DVR_SENSOR_INFO_UPLOAD, [
    ('dwSize', DWORD),
    ('struTime', NET_DVR_TIME_V30),
    ('szSensorName', c_char * 64),
    ('szSensorChan', c_char * 32),
    ('byReboot', BYTE),
    ('byPowerSupply', BYTE),
    ('byStatusType', BYTE),
    ('bySensorType', BYTE),
    ('fVoltageValue', c_float),
    ('fCurrentValue', c_float),
    ('fActualValue', c_float),
    ('szDescription', c_char * 32),
    ('byRes1', BYTE * 128),
])

NET_DVR_SENSOR_INFO_UPLOAD = struct_tagNET_DVR_SENSOR_INFO_UPLOAD
LPNET_DVR_SENSOR_INFO_UPLOAD = POINTER(struct_tagNET_DVR_SENSOR_INFO_UPLOAD)
tagNET_DVR_SENSOR_INFO_UPLOAD = struct_tagNET_DVR_SENSOR_INFO_UPLOAD
