from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_anon_311(Structure):
    pass

_S(struct_anon_311, [
    ('dwAlarmType', DWORD),
    ('byAlarmInputNumber', BYTE * 512),
    ('byRes', BYTE * 160),
])

NET_DVR_ALARMHOST_ALARMINFO = struct_anon_311
LPNET_DVR_ALARMHOST_ALARMINFO = POINTER(struct_anon_311)
