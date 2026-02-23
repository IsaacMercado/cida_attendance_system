from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_matrix_union import NET_MATRIX_UNION


class struct_tagNET_DVR_EXTERNAL_MATRIX_CFG_V50(Structure):
    pass

_S(struct_tagNET_DVR_EXTERNAL_MATRIX_CFG_V50, [
    ('dwSize', DWORD),
    ('byValid', BYTE),
    ('byRes1', BYTE * 3),
    ('sMatrixName', BYTE * 32),
    ('dwMatrixID', DWORD),
    ('wMatrixInputChanNum', WORD),
    ('wMatrixOutputChanNum', WORD),
    ('wMatrixOutputChanRef', WORD * 512),
    ('byMatrixChanType', BYTE),
    ('byMatrixProtocol', BYTE),
    ('byMatrixType', BYTE),
    ('byRes2', BYTE),
    ('struMatrixUnion', NET_MATRIX_UNION),
    ('byRes3', BYTE * 128),
])

NET_DVR_EXTERNAL_MATRIX_CFG_V50 = struct_tagNET_DVR_EXTERNAL_MATRIX_CFG_V50
LPNET_DVR_EXTERNAL_MATRIX_CFG_V50 = POINTER(struct_tagNET_DVR_EXTERNAL_MATRIX_CFG_V50)
tagNET_DVR_EXTERNAL_MATRIX_CFG_V50 = struct_tagNET_DVR_EXTERNAL_MATRIX_CFG_V50
