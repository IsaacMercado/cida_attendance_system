from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_TIME_V30(Structure):
    pass

_S(struct_tagNET_DVR_TIME_V30, [
    ('wYear', WORD),
    ('byMonth', BYTE),
    ('byDay', BYTE),
    ('byHour', BYTE),
    ('byMinute', BYTE),
    ('bySecond', BYTE),
    ('byISO8601', BYTE),
    ('wMilliSec', WORD),
    ('cTimeDifferenceH', c_char),
    ('cTimeDifferenceM', c_char),
])

NET_DVR_TIME_V30 = struct_tagNET_DVR_TIME_V30
LPNET_DVR_TIME_V30 = POINTER(struct_tagNET_DVR_TIME_V30)
tagNET_DVR_TIME_V30 = struct_tagNET_DVR_TIME_V30
