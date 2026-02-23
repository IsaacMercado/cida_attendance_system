from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_matrix_cfg import NET_DVR_MATRIX_CFG


class struct_tagNET_DVR_ANALOGSCREEN(Structure):
    pass

_S(struct_tagNET_DVR_ANALOGSCREEN, [
    ('byDevSerPortNum', BYTE),
    ('byScreenSerPort', BYTE),
    ('byRes', BYTE * 130),
    ('struMatrixCfg', NET_DVR_MATRIX_CFG),
])

NET_DVR_ANALOGSCREEN = struct_tagNET_DVR_ANALOGSCREEN
LPNET_DVR_ANALOGSCREEN = POINTER(struct_tagNET_DVR_ANALOGSCREEN)
tagNET_DVR_ANALOGSCREEN = struct_tagNET_DVR_ANALOGSCREEN
