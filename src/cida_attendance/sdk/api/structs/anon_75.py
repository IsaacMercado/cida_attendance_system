from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_time_ex import NET_DVR_TIME_EX


class struct_anon_75(Structure):
    pass

_S(struct_anon_75, [
    ('dwSize', DWORD),
    ('strStartTime', NET_DVR_TIME_EX),
    ('strStopTime', NET_DVR_TIME_EX),
    ('sLicense', c_char * 32),
    ('dwChannel', DWORD),
    ('byRegion', BYTE),
    ('byRes', BYTE * 127),
])

NET_DVR_VEHICLE_INFO_COND = struct_anon_75
LPNET_DVR_VEHICLE_INFO_COND = POINTER(struct_anon_75)
