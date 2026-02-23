from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_6 import NET_DVR_SCHEDTIME


class struct_tagNET_DVR_WIRELESSDIAL_SCHEDULE(Structure):
    pass

_S(struct_tagNET_DVR_WIRELESSDIAL_SCHEDULE, [
    ('dwSize', DWORD),
    ('struAlarmTime', (NET_DVR_SCHEDTIME * 8) * 7),
    ('struHolidayAlarmTime', NET_DVR_SCHEDTIME * 8),
    ('byRes', BYTE * 128),
])

NET_DVR_WIRELESSDIAL_SCHEDULE = struct_tagNET_DVR_WIRELESSDIAL_SCHEDULE
LPNET_DVR_WIRELESSDIAL_SCHEDULE = POINTER(struct_tagNET_DVR_WIRELESSDIAL_SCHEDULE)
tagNET_DVR_WIRELESSDIAL_SCHEDULE = struct_tagNET_DVR_WIRELESSDIAL_SCHEDULE
