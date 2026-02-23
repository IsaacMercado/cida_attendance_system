from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_anon_60(Structure):
    pass

_S(struct_anon_60, [
    ('dwAlarmType', DWORD),
    ('dwAlarmInputNumber', DWORD),
    ('byAlarmOutputNumber', BYTE * int((32 + 64))),
    ('byAlarmRelateChannel', BYTE * int((32 + 32))),
    ('byChannel', BYTE * int((32 + 32))),
    ('byDiskNumber', BYTE * 33),
    ('byDeviceID', BYTE * 32),
    ('byRes', BYTE * 7),
])

NET_DVR_PUSHALARMINFO_V30 = struct_anon_60
LPNET_DVR_PUSHALARMINFO_V30 = POINTER(struct_anon_60)
