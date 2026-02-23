from ctypes import Structure, c_float

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_108 import NET_DVR_CHANNELSTATE_V30
from .anon_110 import NET_DVR_DISKSTATE


class struct_tagNET_DVR_WORKSTATE_V40(Structure):
    pass

_S(struct_tagNET_DVR_WORKSTATE_V40, [
    ('dwSize', DWORD),
    ('dwDeviceStatic', DWORD),
    ('struHardDiskStatic', NET_DVR_DISKSTATE * 33),
    ('struChanStatic', NET_DVR_CHANNELSTATE_V30 * 512),
    ('dwHasAlarmInStatic', DWORD * int((4096 + 32))),
    ('dwHasAlarmOutStatic', DWORD * int((4096 + 32))),
    ('dwLocalDisplay', DWORD),
    ('byAudioInChanStatus', BYTE * 2),
    ('byRes1', BYTE * 2),
    ('fHumidity', c_float),
    ('fTemperature', c_float),
    ('byRes', BYTE * 116),
])

NET_DVR_WORKSTATE_V40 = struct_tagNET_DVR_WORKSTATE_V40
LPNET_DVR_WORKSTATE_V40 = POINTER(struct_tagNET_DVR_WORKSTATE_V40)
tagNET_DVR_WORKSTATE_V40 = struct_tagNET_DVR_WORKSTATE_V40
