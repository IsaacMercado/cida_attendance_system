from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_MATRIX_CAMERALIST(Structure):
    pass

_S(struct_tagNET_DVR_MATRIX_CAMERALIST, [
    ('dwSize', DWORD),
    ('byRes', BYTE * 12),
    ('dwCamNum', DWORD),
    ('pBuffer', POINTER(BYTE)),
    ('dwBufLen', DWORD),
])

NET_DVR_MATRIX_CAMERALIST = struct_tagNET_DVR_MATRIX_CAMERALIST
LPNET_DVR_MATRIX_CAMERALIST = POINTER(struct_tagNET_DVR_MATRIX_CAMERALIST)
tagNET_DVR_MATRIX_CAMERALIST = struct_tagNET_DVR_MATRIX_CAMERALIST
