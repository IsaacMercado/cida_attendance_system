from ctypes import Structure, c_char, c_int

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_time_ex import NET_DVR_TIME_EX


class struct_tagNET_DVR_GPSALARMINFO(Structure):
    pass

_S(struct_tagNET_DVR_GPSALARMINFO, [
    ('byDeviceID', BYTE * 32),
    ('struGpsTime', NET_DVR_TIME_EX),
    ('dwLongitude', DWORD),
    ('dwLatitude', DWORD),
    ('iTimeZone', c_int),
    ('dwDirection', DWORD),
    ('wSatellites', WORD),
    ('wPrecision', WORD),
    ('dwHeight', DWORD),
    ('dwGPSSeq', DWORD),
    ('wSpeed', WORD),
    ('sDirection', c_char * 2),
    ('byLocateMode', BYTE),
    ('byRes', BYTE * 3),
])

NET_DVR_GPSALARMINFO = struct_tagNET_DVR_GPSALARMINFO
LPNET_DVR_GPSALARMINFO = POINTER(struct_tagNET_DVR_GPSALARMINFO)
tagNET_DVR_GPSALARMINFO = struct_tagNET_DVR_GPSALARMINFO
