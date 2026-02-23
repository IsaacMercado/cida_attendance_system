from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME


class struct_tagNET_DVR_CALIBRATE_TIME(Structure):
    pass

_S(struct_tagNET_DVR_CALIBRATE_TIME, [
    ('dwSize', DWORD),
    ('struTime', NET_DVR_TIME),
    ('wMilliSec', WORD),
    ('byRes', BYTE * 14),
])

NET_DVR_CALIBRATE_TIME = struct_tagNET_DVR_CALIBRATE_TIME
LPNET_DVR_CALIBRATE_TIME = POINTER(struct_tagNET_DVR_CALIBRATE_TIME)
tagNET_DVR_CALIBRATE_TIME = struct_tagNET_DVR_CALIBRATE_TIME
