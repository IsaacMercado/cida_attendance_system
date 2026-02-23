from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER


class struct_anon_1(Structure):
    pass

_S(struct_anon_1, [
    ('dwYear', DWORD),
    ('dwMonth', DWORD),
    ('dwDay', DWORD),
    ('dwHour', DWORD),
    ('dwMinute', DWORD),
    ('dwSecond', DWORD),
])

NET_DVR_TIME = struct_anon_1
LPNET_DVR_TIME = POINTER(struct_anon_1)
