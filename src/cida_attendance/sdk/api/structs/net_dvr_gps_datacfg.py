from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_latitude_param import NET_DVR_LATITUDE_PARAM
from .net_dvr_longitude_param import NET_DVR_LONGITUDE_PARAM


class struct_tagNET_DVR_GPS_DATACFG(Structure):
    pass

_S(struct_tagNET_DVR_GPS_DATACFG, [
    ('dwSize', DWORD),
    ('byGpsDataMode', BYTE),
    ('byLongitudeType', BYTE),
    ('byLatitudeType', BYTE),
    ('byRes', BYTE),
    ('struLatitude', NET_DVR_LATITUDE_PARAM),
    ('struLongitude', NET_DVR_LONGITUDE_PARAM),
    ('byRes1', BYTE * 128),
])

NET_DVR_GPS_DATACFG = struct_tagNET_DVR_GPS_DATACFG
LPNET_DVR_GPS_DATACFG = POINTER(struct_tagNET_DVR_GPS_DATACFG)
tagNET_DVR_GPS_DATACFG = struct_tagNET_DVR_GPS_DATACFG
