from ctypes import Structure

from ..base_classes import _S
from ..ctypes_preamble import POINTER
from .net_dvr_time_v30 import NET_DVR_TIME_V30


class struct_tagNET_DVR_ATTENDANCE_TIME(Structure):
    pass

_S(struct_tagNET_DVR_ATTENDANCE_TIME, [
    ('struOnDutyTime', NET_DVR_TIME_V30),
    ('struOffDutyTime', NET_DVR_TIME_V30),
])

NET_DVR_ATTENDANCE_TIME = struct_tagNET_DVR_ATTENDANCE_TIME
LPNET_DVR_ATTENDANCE_TIME = POINTER(struct_tagNET_DVR_ATTENDANCE_TIME)
tagNET_DVR_ATTENDANCE_TIME = struct_tagNET_DVR_ATTENDANCE_TIME
