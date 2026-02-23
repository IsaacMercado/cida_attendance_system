from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER


class struct_anon_71(Structure):
    pass

_S(struct_anon_71, [
    ('dwAlarmType', DWORD),
    ('dwAlarmInputNumber', DWORD),
    ('dwAlarmOutputNumber', DWORD * 4),
    ('dwAlarmRelateChannel', DWORD * 16),
    ('dwChannel', DWORD * 16),
    ('dwDiskNumber', DWORD * 16),
])

NET_DVR_ALARMINFO = struct_anon_71
LPNET_DVR_ALARMINFO = POINTER(struct_anon_71)
