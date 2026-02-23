from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_GPS_INFO(Structure):
    pass

_S(struct_tagNET_DVR_GPS_INFO, [
    ('byDirection', BYTE * 2),
    ('bySvs', BYTE),
    ('byLocateMode', BYTE),
    ('wHDOP', WORD),
    ('wHeight', WORD),
    ('dwLatitude', DWORD),
    ('dwLongitude', DWORD),
    ('dwVehicleSpeed', DWORD),
    ('dwVehicleDirection', DWORD),
    ('byRes', BYTE * 8),
])

NET_DVR_GPS_INFO = struct_tagNET_DVR_GPS_INFO
LPNET_DVR_GPS_INFO = POINTER(struct_tagNET_DVR_GPS_INFO)
tagNET_DVR_GPS_INFO = struct_tagNET_DVR_GPS_INFO
