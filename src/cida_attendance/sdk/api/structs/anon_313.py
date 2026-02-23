from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME


class struct_anon_313(Structure):
    pass

_S(struct_anon_313, [
    ('sFileName', c_char * 64),
    ('struTime', NET_DVR_TIME),
    ('dwFileSize', DWORD),
    ('sCardNum', c_char * 40),
    ('byPlateColor', BYTE),
    ('byVehicleLogo', BYTE),
    ('byEventSearchStatus', BYTE),
    ('byRecogResult', BYTE),
    ('sLicense', c_char * 16),
    ('byRes', BYTE * 12),
])

NET_DVR_FIND_PICTURE = struct_anon_313
LPNET_DVR_FIND_PICTURE = POINTER(struct_anon_313)
