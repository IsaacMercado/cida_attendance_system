from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_TIME_V50(Structure):
    pass

_S(struct_tagNET_DVR_TIME_V50, [
    ('wYear', WORD),
    ('byMonth', BYTE),
    ('byDay', BYTE),
    ('byHour', BYTE),
    ('byMinute', BYTE),
    ('bySecond', BYTE),
    ('byISO8601', BYTE),
    ('wMillisecond', WORD),
    ('cTimeDifferenceH', c_char),
    ('cTimeDifferenceM', c_char),
])

NET_DVR_TIME_V50 = struct_tagNET_DVR_TIME_V50
LPNET_DVR_TIME_V50 = POINTER(struct_tagNET_DVR_TIME_V50)
tagNET_DVR_TIME_V50 = struct_tagNET_DVR_TIME_V50
