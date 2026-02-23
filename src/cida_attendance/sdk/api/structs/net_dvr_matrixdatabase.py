from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_MATRIXDATABASE(Structure):
    pass

_S(struct_tagNET_DVR_MATRIXDATABASE, [
    ('dwDevType', DWORD),
    ('dwParam', DWORD),
    ('byFileType', BYTE),
    ('byRes', BYTE * 3),
])

NET_DVR_MATRIXDATABASE = struct_tagNET_DVR_MATRIXDATABASE
LPNET_DVR_MATRIXDATABASE = POINTER(struct_tagNET_DVR_MATRIXDATABASE)
tagNET_DVR_MATRIXDATABASE = struct_tagNET_DVR_MATRIXDATABASE
