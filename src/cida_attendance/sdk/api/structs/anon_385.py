from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_anon_385(Structure):
    pass

_S(struct_anon_385, [
    ('byHour', BYTE),
    ('byMinute', BYTE),
    ('bySecond', BYTE),
    ('byRes', BYTE),
    ('wMilliSecond', WORD),
    ('byRes1', BYTE * 2),
])

NET_DVR_DAYTIME = struct_anon_385
LPNET_DVR_DAYTIME = POINTER(struct_anon_385)
