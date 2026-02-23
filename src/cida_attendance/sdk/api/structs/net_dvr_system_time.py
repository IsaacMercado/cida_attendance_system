from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SYSTEM_TIME(Structure):
    pass

_S(struct_tagNET_DVR_SYSTEM_TIME, [
    ('wYear', WORD),
    ('wMonth', WORD),
    ('wDay', WORD),
    ('wHour', WORD),
    ('wMinute', WORD),
    ('wSecond', WORD),
    ('wMilliSec', WORD),
    ('byRes', BYTE * 2),
])

NET_DVR_SYSTEM_TIME = struct_tagNET_DVR_SYSTEM_TIME
LPNET_DVR_SYSTEM_TIME = POINTER(struct_tagNET_DVR_SYSTEM_TIME)
tagNET_DVR_SYSTEM_TIME = struct_tagNET_DVR_SYSTEM_TIME
