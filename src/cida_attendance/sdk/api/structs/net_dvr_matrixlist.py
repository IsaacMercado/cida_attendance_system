from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_MATRIXLIST(Structure):
    pass

_S(struct_tagNET_DVR_MATRIXLIST, [
    ('dwSize', DWORD),
    ('byRes', BYTE * 12),
    ('dwMatrixNum', DWORD),
    ('pBuffer', POINTER(BYTE)),
    ('dwBufLen', DWORD),
])

NET_DVR_MATRIXLIST = struct_tagNET_DVR_MATRIXLIST
LPNET_DVR_MATRIXLIST = POINTER(struct_tagNET_DVR_MATRIXLIST)
tagNET_DVR_MATRIXLIST = struct_tagNET_DVR_MATRIXLIST
