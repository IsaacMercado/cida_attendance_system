from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_6 import NET_DVR_SCHEDTIME


class struct_anon_393(Structure):
    pass

_S(struct_anon_393, [
    ('dwEnableVILostAlarm', DWORD),
    ('dwHandleType', DWORD),
    ('dwMaxRelAlarmOutChanNum', DWORD),
    ('dwRelAlarmOut', DWORD * int((4096 + 32))),
    ('struAlarmTime', (NET_DVR_SCHEDTIME * 8) * 7),
    ('byVILostAlarmThreshold', BYTE),
    ('byRes', BYTE * 63),
])

NET_DVR_VILOST_V40 = struct_anon_393
LPNET_DVR_VILOST_V40 = POINTER(struct_anon_393)
