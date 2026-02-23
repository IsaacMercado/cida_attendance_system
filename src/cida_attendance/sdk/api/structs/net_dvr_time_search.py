from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_TIME_SEARCH(Structure):
    pass

_S(struct_tagNET_DVR_TIME_SEARCH, [
    ('wYear', WORD),
    ('byMonth', BYTE),
    ('byDay', BYTE),
    ('byHour', BYTE),
    ('byMinute', BYTE),
    ('bySecond', BYTE),
    ('cTimeDifferenceH', c_char),
    ('cTimeDifferenceM', c_char),
    ('byLocalOrUTC', BYTE),
    ('wMillisecond', WORD),
])

NET_DVR_TIME_SEARCH = struct_tagNET_DVR_TIME_SEARCH
LPNET_DVR_TIME_SEARCH = POINTER(struct_tagNET_DVR_TIME_SEARCH)
tagNET_DVR_TIME_SEARCH = struct_tagNET_DVR_TIME_SEARCH
