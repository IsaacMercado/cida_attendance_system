from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_park_info import NET_DVR_PARK_INFO
from .net_dvr_time_ex import NET_DVR_TIME_EX
from .net_vca_dev_info import NET_VCA_DEV_INFO


class struct_tagNET_DVR_CROSSLINE_ALARM(Structure):
    pass

_S(struct_tagNET_DVR_CROSSLINE_ALARM, [
    ('dwSize', DWORD),
    ('struDevInfo', NET_VCA_DEV_INFO),
    ('struTriggerTime', NET_DVR_TIME_EX),
    ('struParkInfo', NET_DVR_PARK_INFO),
    ('byRes1', BYTE * 128),
])

NET_DVR_CROSSLINE_ALARM = struct_tagNET_DVR_CROSSLINE_ALARM
LPNET_DVR_CROSSLINE_ALARM = POINTER(struct_tagNET_DVR_CROSSLINE_ALARM)
tagNET_DVR_CROSSLINE_ALARM = struct_tagNET_DVR_CROSSLINE_ALARM
