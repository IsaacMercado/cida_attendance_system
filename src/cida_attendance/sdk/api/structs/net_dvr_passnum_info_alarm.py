from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR
from .net_dvr_time_v30 import NET_DVR_TIME_V30


class struct_tagNET_DVR_PASSNUM_INFO_ALARM(Structure):
    pass

_S(struct_tagNET_DVR_PASSNUM_INFO_ALARM, [
    ('dwSize', DWORD),
    ('dwAccessChannel', DWORD),
    ('struSwipeTime', NET_DVR_TIME_V30),
    ('byNetUser', BYTE * 16),
    ('struRemoteHostAddr', NET_DVR_IPADDR),
    ('dwEntryTimes', DWORD),
    ('dwExitTimes', DWORD),
    ('dwTotalTimes', DWORD),
    ('byRes', BYTE * 300),
])

NET_DVR_PASSNUM_INFO_ALARM = struct_tagNET_DVR_PASSNUM_INFO_ALARM
LPNET_DVR_PASSNUM_INFO_ALARM = POINTER(struct_tagNET_DVR_PASSNUM_INFO_ALARM)
tagNET_DVR_PASSNUM_INFO_ALARM = struct_tagNET_DVR_PASSNUM_INFO_ALARM
