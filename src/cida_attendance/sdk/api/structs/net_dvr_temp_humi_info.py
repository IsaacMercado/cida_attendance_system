from ctypes import Structure, c_float

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_time_v30 import NET_DVR_TIME_V30


class struct_tagNET_DVR_TEMP_HUMI_INFO(Structure):
    pass

_S(struct_tagNET_DVR_TEMP_HUMI_INFO, [
    ('dwSize', DWORD),
    ('struCurrentTime', NET_DVR_TIME_V30),
    ('fTemperature', c_float),
    ('fHumidity', c_float),
    ('byRes', BYTE * 256),
])

NET_DVR_TEMP_HUMI_INFO = struct_tagNET_DVR_TEMP_HUMI_INFO
LPNET_DVR_TEMP_HUMI_INFO = POINTER(struct_tagNET_DVR_TEMP_HUMI_INFO)
tagNET_DVR_TEMP_HUMI_INFO = struct_tagNET_DVR_TEMP_HUMI_INFO
