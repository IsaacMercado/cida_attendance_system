from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_anon_70(Structure):
    pass

_S(struct_anon_70, [
    ('dwAlarmType', DWORD),
    ('dwAlarmInputNumber', DWORD),
    ('byAlarmOutputNumber', BYTE * int((32 + 64))),
    ('byAlarmRelateChannel', BYTE * int((32 + 32))),
    ('byChannel', BYTE * int((32 + 32))),
    ('byDiskNumber', BYTE * 33),
])

NET_DVR_ALARMINFO_V30 = struct_anon_70
LPNET_DVR_ALARMINFO_V30 = POINTER(struct_anon_70)
