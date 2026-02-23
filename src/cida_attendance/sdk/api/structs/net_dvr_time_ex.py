from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_TIME_EX(Structure):
    pass

_S(struct_tagNET_DVR_TIME_EX, [
    ('wYear', WORD),
    ('byMonth', BYTE),
    ('byDay', BYTE),
    ('byHour', BYTE),
    ('byMinute', BYTE),
    ('bySecond', BYTE),
    ('byRes', BYTE),
])

NET_DVR_TIME_EX = struct_tagNET_DVR_TIME_EX
LPNET_DVR_TIME_EX = POINTER(struct_tagNET_DVR_TIME_EX)
tagNET_DVR_TIME_EX = struct_tagNET_DVR_TIME_EX
