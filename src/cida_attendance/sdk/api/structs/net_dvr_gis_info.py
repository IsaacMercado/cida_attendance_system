from ctypes import Structure, c_float

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_453 import NET_DVR_PTZPOS_PARAM
from .net_dvr_lli_param import NET_DVR_LLI_PARAM
from .net_dvr_sensor_param import NET_DVR_SENSOR_PARAM
from .net_ptz_info import NET_PTZ_INFO


class struct_tagNET_DVR_GIS_INFO(Structure):
    pass

_S(struct_tagNET_DVR_GIS_INFO, [
    ('dwSize', DWORD),
    ('fAzimuth', c_float),
    ('fHorizontalValue', c_float),
    ('fVerticalValue', c_float),
    ('fVisibleRadius', c_float),
    ('fMaxViewRadius', c_float),
    ('byLatitudeType', BYTE),
    ('byLongitudeType', BYTE),
    ('byPTZPosExEnable', BYTE),
    ('byRes1', BYTE),
    ('struLatitude', NET_DVR_LLI_PARAM),
    ('struLongitude', NET_DVR_LLI_PARAM),
    ('struPtzPos', NET_DVR_PTZPOS_PARAM),
    ('struSensorParam', NET_DVR_SENSOR_PARAM),
    ('struPtzPosEx', NET_PTZ_INFO),
    ('fMinHorizontalValue', c_float),
    ('fMaxHorizontalValue', c_float),
    ('fMinVerticalValue', c_float),
    ('fMaxVerticalValue', c_float),
    ('byRes', BYTE * 220),
])

NET_DVR_GIS_INFO = struct_tagNET_DVR_GIS_INFO
LPNET_DVR_GIS_INFO = POINTER(struct_tagNET_DVR_GIS_INFO)
tagNET_DVR_GIS_INFO = struct_tagNET_DVR_GIS_INFO
