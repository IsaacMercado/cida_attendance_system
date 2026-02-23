from ctypes import Structure, c_int

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_gps_info import NET_DVR_GPS_INFO
from .net_dvr_time_v30 import NET_DVR_TIME_V30


class struct__NET_DVR_GPS_STATUS_ALARM_(Structure):
    pass

_S(struct__NET_DVR_GPS_STATUS_ALARM_, [
    ('dwSize', DWORD),
    ('struGPSTime', NET_DVR_TIME_V30),
    ('struGPSInfo', NET_DVR_GPS_INFO),
    ('byRetransFlag', BYTE),
    ('byNeedsResponse', BYTE),
    ('byType', BYTE),
    ('byBatteryRemaining', BYTE),
    ('iRollAngle', c_int),
    ('iPitchAngle', c_int),
    ('wRelativeHeight', WORD),
    ('wVerticalSpeed', WORD),
    ('byRes2', BYTE * 160),
])

NET_DVR_GPS_STATUS_ALARM = struct__NET_DVR_GPS_STATUS_ALARM_
LPNET_DVR_GPS_STATUS_ALARM = POINTER(struct__NET_DVR_GPS_STATUS_ALARM_)
_NET_DVR_GPS_STATUS_ALARM_ = struct__NET_DVR_GPS_STATUS_ALARM_
