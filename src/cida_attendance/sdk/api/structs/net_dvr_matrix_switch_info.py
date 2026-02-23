from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_MATRIX_SWITCH_INFO(Structure):
    pass

_S(struct_tagNET_DVR_MATRIX_SWITCH_INFO, [
    ('dwSize', DWORD),
    ('dwInputChan', DWORD),
    ('dwOutputChan', DWORD),
    ('dwMatrixID', DWORD),
    ('byRes', BYTE * 28),
])

NET_DVR_MATRIX_SWITCH_INFO = struct_tagNET_DVR_MATRIX_SWITCH_INFO
LPNET_DVR_MATRIX_SWITCH_INFO = POINTER(struct_tagNET_DVR_MATRIX_SWITCH_INFO)
tagNET_DVR_MATRIX_SWITCH_INFO = struct_tagNET_DVR_MATRIX_SWITCH_INFO
