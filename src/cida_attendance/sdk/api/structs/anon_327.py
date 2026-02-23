from ctypes import Structure

from ..base_classes import _S, BYTE, LONG
from .anon_1 import NET_DVR_TIME


class struct_anon_327(Structure):
    pass

_S(struct_anon_327, [
    ('lChannel', LONG),
    ('struStartTime', NET_DVR_TIME),
    ('struStopTime', NET_DVR_TIME),
    ('byRes', BYTE * 48),
])

