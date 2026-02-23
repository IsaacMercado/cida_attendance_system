from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME


class struct_tagNET_DVR_FINDDATA_PCNVR(Structure):
    pass

_S(struct_tagNET_DVR_FINDDATA_PCNVR, [
    ('sFileName', c_char * 100),
    ('struStartTime', NET_DVR_TIME),
    ('struStopTime', NET_DVR_TIME),
    ('dwFileSize', DWORD),
    ('sCardNum', c_char * 40),
    ('byLocked', BYTE),
    ('byFileType', BYTE),
    ('byRes', BYTE * 2),
])

NET_DVR_FINDDATA_PCNVR = struct_tagNET_DVR_FINDDATA_PCNVR
LPNET_DVR_FINDDATA_PCNVR = POINTER(struct_tagNET_DVR_FINDDATA_PCNVR)
tagNET_DVR_FINDDATA_PCNVR = struct_tagNET_DVR_FINDDATA_PCNVR
