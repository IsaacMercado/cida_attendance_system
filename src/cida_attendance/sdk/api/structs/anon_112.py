from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_109 import NET_DVR_CHANNELSTATE
from .anon_110 import NET_DVR_DISKSTATE


class struct_anon_112(Structure):
    pass

_S(struct_anon_112, [
    ('dwDeviceStatic', DWORD),
    ('struHardDiskStatic', NET_DVR_DISKSTATE * 16),
    ('struChanStatic', NET_DVR_CHANNELSTATE * 16),
    ('byAlarmInStatic', BYTE * 16),
    ('byAlarmOutStatic', BYTE * 4),
    ('dwLocalDisplay', DWORD),
])

NET_DVR_WORKSTATE = struct_anon_112
LPNET_DVR_WORKSTATE = POINTER(struct_anon_112)
