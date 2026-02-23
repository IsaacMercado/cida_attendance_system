from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_6 import NET_DVR_SCHEDTIME


class struct_anon_90(Structure):
    pass

_S(struct_anon_90, [
    ('dwSize', DWORD),
    ('sAlarmOutName', BYTE * 32),
    ('dwAlarmOutDelay', DWORD),
    ('struAlarmOutTime', (NET_DVR_SCHEDTIME * 8) * 7),
    ('byAlarmOutHandle', BYTE),
    ('byNormalSatus', BYTE),
    ('byRes', BYTE * 14),
])

NET_DVR_ALARMOUTCFG_V30 = struct_anon_90
LPNET_DVR_ALARMOUTCFG_V30 = POINTER(struct_anon_90)
