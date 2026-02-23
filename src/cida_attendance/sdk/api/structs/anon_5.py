from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR
from .net_dvr_time_v50 import NET_DVR_TIME_V50


class struct_anon_5(Structure):
    pass

_S(struct_anon_5, [
    ('struLogTime', NET_DVR_TIME_V50),
    ('dwMajorType', DWORD),
    ('dwMinorType', DWORD),
    ('sPanelUser', BYTE * 16),
    ('sNetUser', BYTE * 16),
    ('struRemoteHostAddr', NET_DVR_IPADDR),
    ('dwParaType', DWORD),
    ('dwChannel', DWORD),
    ('dwDiskNumber', DWORD),
    ('dwAlarmInPort', DWORD),
    ('dwAlarmOutPort', DWORD),
    ('dwInfoLen', DWORD),
    ('sInfo', c_char * 11840),
    ('byRes', BYTE * 128),
])

NET_DVR_LOG_V50 = struct_anon_5
LPNET_DVR_LOG_V50 = POINTER(struct_anon_5)
