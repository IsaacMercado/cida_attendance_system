from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_51 import NET_DVR_SINGLE_RS232


class struct_tagNET_MATRIX_ANALOGMATRIX(Structure):
    pass

_S(struct_tagNET_MATRIX_ANALOGMATRIX, [
    ('bySerPortNum', BYTE),
    ('byMatrixSerPortType', BYTE),
    ('byRes1', BYTE * 2),
    ('struRS232', NET_DVR_SINGLE_RS232),
    ('byRes2', BYTE * 200),
])

NET_MATRIX_ANALOGMATRIX = struct_tagNET_MATRIX_ANALOGMATRIX
LPNET_MATRIX_ANALOGMATRIX = POINTER(struct_tagNET_MATRIX_ANALOGMATRIX)
tagNET_MATRIX_ANALOGMATRIX = struct_tagNET_MATRIX_ANALOGMATRIX
