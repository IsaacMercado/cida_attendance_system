from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_matrix_union import NET_MATRIX_UNION


class struct_tagNET_DVR_EXTERNAL_MATRIX_CFG(Structure):
    pass

_S(struct_tagNET_DVR_EXTERNAL_MATRIX_CFG, [
    ('dwSize', DWORD),
    ('byValid', BYTE),
    ('byRes1', BYTE * 3),
    ('sMatrixName', BYTE * 32),
    ('dwMatrixID', DWORD),
    ('wMatrixInputChanNum', WORD),
    ('wMatrixOutputChanNum', WORD),
    ('wMatrixOutputChanRef', WORD * 224),
    ('byMatrixChanType', BYTE),
    ('byMatrixProtocol', BYTE),
    ('byMatrixType', BYTE),
    ('byRes2', BYTE),
    ('struMatrixUnion', NET_MATRIX_UNION),
    ('byRes3', BYTE * 128),
])

NET_DVR_EXTERNAL_MATRIX_CFG = struct_tagNET_DVR_EXTERNAL_MATRIX_CFG
LPNET_DVR_EXTERNAL_MATRIX_CFG = POINTER(struct_tagNET_DVR_EXTERNAL_MATRIX_CFG)
tagNET_DVR_EXTERNAL_MATRIX_CFG = struct_tagNET_DVR_EXTERNAL_MATRIX_CFG
