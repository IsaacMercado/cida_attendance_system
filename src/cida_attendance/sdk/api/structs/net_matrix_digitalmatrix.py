from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_MATRIX_DIGITALMATRIX(Structure):
    pass

_S(struct_tagNET_MATRIX_DIGITALMATRIX, [
    ('struAddress', NET_DVR_IPADDR),
    ('wPort', WORD),
    ('byNicNum', BYTE),
    ('byRes', BYTE * 69),
])

NET_MATRIX_DIGITALMATRIX = struct_tagNET_MATRIX_DIGITALMATRIX
LPNET_MATRIX_DIGITALMATRIX = POINTER(struct_tagNET_MATRIX_DIGITALMATRIX)
tagNET_MATRIX_DIGITALMATRIX = struct_tagNET_MATRIX_DIGITALMATRIX
