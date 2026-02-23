from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME


class struct_anon_202(Structure):
    pass

_S(struct_anon_202, [
    ('sFileName', c_char * 100),
    ('struStartTime', NET_DVR_TIME),
    ('struStopTime', NET_DVR_TIME),
    ('dwFileSize', DWORD),
    ('sCardNum', c_char * 32),
    ('byLocked', BYTE),
    ('byFileType', BYTE),
    ('byRes', BYTE * 2),
])

NET_DVR_FINDDATA_V30 = struct_anon_202
LPNET_DVR_FINDDATA_V30 = POINTER(struct_anon_202)
