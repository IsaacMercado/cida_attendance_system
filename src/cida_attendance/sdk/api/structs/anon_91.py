from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_6 import NET_DVR_SCHEDTIME


class struct_anon_91(Structure):
    pass

_S(struct_anon_91, [
    ('dwSize', DWORD),
    ('sAlarmOutName', BYTE * 32),
    ('dwAlarmOutDelay', DWORD),
    ('struAlarmOutTime', (NET_DVR_SCHEDTIME * 4) * 7),
])

NET_DVR_ALARMOUTCFG = struct_anon_91
LPNET_DVR_ALARMOUTCFG = POINTER(struct_anon_91)
