from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_MATRIX_MONITORLIST(Structure):
    pass

_S(struct_tagNET_DVR_MATRIX_MONITORLIST, [
    ('dwSize', DWORD),
    ('byRes', BYTE * 12),
    ('dwMonNum', DWORD),
    ('pBuffer', POINTER(BYTE)),
    ('dwBufLen', DWORD),
])

NET_DVR_MATRIX_MONITORLIST = struct_tagNET_DVR_MATRIX_MONITORLIST
LPNET_DVR_MATRIX_MONITORLIST = POINTER(struct_tagNET_DVR_MATRIX_MONITORLIST)
tagNET_DVR_MATRIX_MONITORLIST = struct_tagNET_DVR_MATRIX_MONITORLIST
