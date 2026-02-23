from ctypes import Structure, c_float

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_453 import NET_DVR_PTZPOS_PARAM
from .net_dvr_lli_param import NET_DVR_LLI_PARAM
from .net_dvr_sensor_param import NET_DVR_SENSOR_PARAM
from .net_vca_dev_info import NET_VCA_DEV_INFO


class struct_tagNET_DVR_GIS_UPLOADINFO(Structure):
    pass

_S(struct_tagNET_DVR_GIS_UPLOADINFO, [
    ('dwSize', DWORD),
    ('dwRelativeTime', DWORD),
    ('dwAbsTime', DWORD),
    ('struDevInfo', NET_VCA_DEV_INFO),
    ('fAzimuth', c_float),
    ('byLatitudeType', BYTE),
    ('byLongitudeType', BYTE),
    ('byRes1', BYTE * 2),
    ('struLatitude', NET_DVR_LLI_PARAM),
    ('struLongitude', NET_DVR_LLI_PARAM),
    ('fHorizontalValue', c_float),
    ('fVerticalValue', c_float),
    ('fVisibleRadius', c_float),
    ('fMaxViewRadius', c_float),
    ('struSensorParam', NET_DVR_SENSOR_PARAM),
    ('struPtzPos', NET_DVR_PTZPOS_PARAM),
    ('byRes', BYTE * 256),
])

NET_DVR_GIS_UPLOADINFO = struct_tagNET_DVR_GIS_UPLOADINFO
LPNET_DVR_GIS_UPLOADINFO = POINTER(struct_tagNET_DVR_GIS_UPLOADINFO)
tagNET_DVR_GIS_UPLOADINFO = struct_tagNET_DVR_GIS_UPLOADINFO
