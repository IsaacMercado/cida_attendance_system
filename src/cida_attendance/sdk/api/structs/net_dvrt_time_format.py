from ctypes import Structure, c_char

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVRT_TIME_FORMAT(Structure):
    pass

_S(struct_tagNET_DVRT_TIME_FORMAT, [
    ('byTimeForm', BYTE),
    ('byRes1', BYTE * 23),
    ('byHourMode', BYTE),
    ('byRes2', BYTE * 3),
    ('chSeprator', c_char * 4),
    ('chDisplaySeprator', c_char * 4),
    ('byDisplayForm', BYTE),
    ('byRes3', BYTE * 3),
    ('byDisplayHourMode', BYTE),
    ('byRes4', BYTE * 19),
])

NET_DVR_TIME_FORMAT = struct_tagNET_DVRT_TIME_FORMAT
LPNET_DVR_TIME_FORMAT = POINTER(struct_tagNET_DVRT_TIME_FORMAT)
tagNET_DVRT_TIME_FORMAT = struct_tagNET_DVRT_TIME_FORMAT
