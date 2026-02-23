from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_TIME_SEARCH_COND(Structure):
    pass

_S(struct_tagNET_DVR_TIME_SEARCH_COND, [
    ('wYear', WORD),
    ('byMonth', BYTE),
    ('byDay', BYTE),
    ('byHour', BYTE),
    ('byMinute', BYTE),
    ('bySecond', BYTE),
    ('byLocalOrUTC', BYTE),
    ('wMillisecond', WORD),
    ('cTimeDifferenceH', c_char),
    ('cTimeDifferenceM', c_char),
])

NET_DVR_TIME_SEARCH_COND = struct_tagNET_DVR_TIME_SEARCH_COND
LPNET_DVR_TIME_SEARCH_COND = POINTER(struct_tagNET_DVR_TIME_SEARCH_COND)
tagNET_DVR_TIME_SEARCH_COND = struct_tagNET_DVR_TIME_SEARCH_COND
