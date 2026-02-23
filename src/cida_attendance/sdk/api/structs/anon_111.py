from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_108 import NET_DVR_CHANNELSTATE_V30
from .anon_110 import NET_DVR_DISKSTATE


class struct_anon_111(Structure):
    pass

_S(struct_anon_111, [
    ('dwDeviceStatic', DWORD),
    ('struHardDiskStatic', NET_DVR_DISKSTATE * 33),
    ('struChanStatic', NET_DVR_CHANNELSTATE_V30 * int((32 + 32))),
    ('byAlarmInStatic', BYTE * int((32 + 128))),
    ('byAlarmOutStatic', BYTE * int((32 + 64))),
    ('dwLocalDisplay', DWORD),
    ('byAudioChanStatus', BYTE * 2),
    ('byRes', BYTE * 10),
])

NET_DVR_WORKSTATE_V30 = struct_anon_111
LPNET_DVR_WORKSTATE_V30 = POINTER(struct_anon_111)
