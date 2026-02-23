from ctypes import Structure

from ..base_classes import _S, BYTE
from .anon_1 import NET_DVR_TIME


class struct_anon_353(Structure):
    pass

_S(struct_anon_353, [
    ('struTimePoint', NET_DVR_TIME),
    ('byRes', BYTE * 104),
])

