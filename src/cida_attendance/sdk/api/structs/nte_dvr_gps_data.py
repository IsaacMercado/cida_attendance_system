from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME
from .net_dvr_gps_info import NET_DVR_GPS_INFO


class struct_tagNTE_DVR_GPS_DATA(Structure):
    pass

_S(struct_tagNTE_DVR_GPS_DATA, [
    ('struGPSInfo', NET_DVR_GPS_INFO),
    ('struTime', NET_DVR_TIME),
    ('byRes', BYTE * 12),
])

NET_DVR_GPS_DATA = struct_tagNTE_DVR_GPS_DATA
LPNET_DVR_GPS_DATA = POINTER(struct_tagNTE_DVR_GPS_DATA)
tagNTE_DVR_GPS_DATA = struct_tagNTE_DVR_GPS_DATA
