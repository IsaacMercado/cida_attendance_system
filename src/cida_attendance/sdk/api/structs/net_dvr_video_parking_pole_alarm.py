from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_time_v30 import NET_DVR_TIME_V30


class struct__NET_DVR_VIDEO_PARKING_POLE_ALARM_(Structure):
    pass

_S(struct__NET_DVR_VIDEO_PARKING_POLE_ALARM_, [
    ('dwSize', DWORD),
    ('struTime', NET_DVR_TIME_V30),
    ('byParkingNum', BYTE * 32),
    ('byAlarmType', BYTE),
    ('byVehicleEnterState', BYTE),
    ('byRes', BYTE * 78),
])

NET_DVR_VIDEO_PARKING_POLE_ALARM = struct__NET_DVR_VIDEO_PARKING_POLE_ALARM_
LPNET_DVR_VIDEO_PARKING_POLE_ALARM = POINTER(struct__NET_DVR_VIDEO_PARKING_POLE_ALARM_)
_NET_DVR_VIDEO_PARKING_POLE_ALARM_ = struct__NET_DVR_VIDEO_PARKING_POLE_ALARM_
