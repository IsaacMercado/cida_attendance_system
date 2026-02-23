from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from .anon_1 import NET_DVR_TIME


class struct_anon_352(Structure):
    pass

_S(struct_anon_352, [
    ('struBeginTime', NET_DVR_TIME),
    ('struEndTime', NET_DVR_TIME),
    ('dwInterval', DWORD),
    ('byRes', BYTE * 76),
])

