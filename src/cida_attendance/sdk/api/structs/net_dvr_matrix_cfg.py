from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_MATRIX_CFG(Structure):
    pass

_S(struct_tagNET_DVR_MATRIX_CFG, [
    ('byValid', BYTE),
    ('byCommandProtocol', BYTE),
    ('byScreenType', BYTE),
    ('byRes1', BYTE),
    ('byScreenToMatrix', BYTE * 32),
    ('byRes2', BYTE * 4),
])

NET_DVR_MATRIX_CFG = struct_tagNET_DVR_MATRIX_CFG
LPNET_DVR_MATRIX_CFG = POINTER(struct_tagNET_DVR_MATRIX_CFG)
tagNET_DVR_MATRIX_CFG = struct_tagNET_DVR_MATRIX_CFG
