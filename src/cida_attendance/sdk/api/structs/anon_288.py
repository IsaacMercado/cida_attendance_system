from ctypes import Structure, c_char

from ..base_classes import _S, BYTE
from .anon_1 import NET_DVR_TIME


class struct_anon_288(Structure):
    pass

_S(struct_anon_288, [
    ('tmStart', NET_DVR_TIME),
    ('tmEnd', NET_DVR_TIME),
    ('byTimeDifferenceFlag', BYTE),
    ('cStartTimeDifferenceH', c_char),
    ('cStartTimeDifferenceM', c_char),
    ('cStopTimeDifferenceH', c_char),
    ('cStopTimeDifferenceM', c_char),
    ('byRes', BYTE * 87),
])

