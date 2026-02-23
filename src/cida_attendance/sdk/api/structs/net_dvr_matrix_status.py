from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_matrix_subboard import NET_DVR_MATRIX_SUBBOARD


class struct_tagNET_DVR_MATRIX_STATUS(Structure):
    pass

_S(struct_tagNET_DVR_MATRIX_STATUS, [
    ('dwSize', DWORD),
    ('byMainFrameType', BYTE),
    ('bySoltNum', BYTE),
    ('byBoardNum', BYTE),
    ('byRes', BYTE),
    ('struMatrixSubboard', NET_DVR_MATRIX_SUBBOARD * 16),
    ('byRes2', BYTE * 48),
])

NET_DVR_MATRIX_STATUS = struct_tagNET_DVR_MATRIX_STATUS
LPNET_DVR_MATRIX_STATUS = POINTER(struct_tagNET_DVR_MATRIX_STATUS)
tagNET_DVR_MATRIX_STATUS = struct_tagNET_DVR_MATRIX_STATUS
