from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME


class struct_anon_203(Structure):
    pass

_S(struct_anon_203, [
    ('sFileName', c_char * 100),
    ('struStartTime', NET_DVR_TIME),
    ('struStopTime', NET_DVR_TIME),
    ('dwFileSize', DWORD),
    ('sCardNum', c_char * 32),
    ('byLocked', BYTE),
    ('byFileType', BYTE),
    ('byQuickSearch', BYTE),
    ('byRes', BYTE),
    ('dwFileIndex', DWORD),
    ('byStreamType', BYTE),
    ('byRes1', BYTE * 127),
])

NET_DVR_FINDDATA_V40 = struct_anon_203
LPNET_DVR_FINDDATA_V40 = POINTER(struct_anon_203)
