from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from .anon_1 import NET_DVR_TIME


class struct_anon_126(Structure):
    pass

_S(struct_anon_126, [
    ('dwChannel', DWORD),
    ('sUserName', BYTE * 32),
    ('sPassword', BYTE * 16),
    ('struStartTime', NET_DVR_TIME),
    ('struStopTime', NET_DVR_TIME),
])

