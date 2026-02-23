from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_6 import NET_DVR_SCHEDTIME


class struct_tagNET_DVR_EVENT_SCHEDULE(Structure):
    pass

_S(struct_tagNET_DVR_EVENT_SCHEDULE, [
    ('dwSize', DWORD),
    ('struAlarmTime', (NET_DVR_SCHEDTIME * 8) * 7),
    ('struHolidayAlarmTime', NET_DVR_SCHEDTIME * 8),
    ('bySceneID', (BYTE * 8) * 7),
    ('byRes', BYTE * 72),
])

NET_DVR_EVENT_SCHEDULE = struct_tagNET_DVR_EVENT_SCHEDULE
LPNET_DVR_EVENT_SCHEDULE = POINTER(struct_tagNET_DVR_EVENT_SCHEDULE)
tagNET_DVR_EVENT_SCHEDULE = struct_tagNET_DVR_EVENT_SCHEDULE
