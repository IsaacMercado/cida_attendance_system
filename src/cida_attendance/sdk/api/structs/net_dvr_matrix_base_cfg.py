from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_MATRIX_BASE_CFG(Structure):
    pass

_S(struct_tagNET_DVR_MATRIX_BASE_CFG, [
    ('dwSize', DWORD),
    ('dwValidInputNum', DWORD),
    ('dwValidOutputNum', DWORD),
    ('byRes', BYTE * 64),
])

NET_DVR_MATRIX_BASE_CFG = struct_tagNET_DVR_MATRIX_BASE_CFG
LPNET_DVR_MATRIX_BASE_CFG = POINTER(struct_tagNET_DVR_MATRIX_BASE_CFG)
tagNET_DVR_MATRIX_BASE_CFG = struct_tagNET_DVR_MATRIX_BASE_CFG
