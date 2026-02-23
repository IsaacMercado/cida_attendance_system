from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_MATRIX_LOGO_CFG(Structure):
    pass

_S(struct_tagNET_DVR_MATRIX_LOGO_CFG, [
    ('dwSize', DWORD),
    ('byExist', BYTE),
    ('byRes1', BYTE * 3),
    ('dwLogoSize', DWORD),
    ('byLogoName', BYTE * 32),
    ('dwLogoNo', DWORD),
    ('byRes2', BYTE * 28),
])

NET_DVR_MATRIX_LOGO_CFG = struct_tagNET_DVR_MATRIX_LOGO_CFG
LPNET_DVR_MATRIX_LOGO_CFG = POINTER(struct_tagNET_DVR_MATRIX_LOGO_CFG)
tagNET_DVR_MATRIX_LOGO_CFG = struct_tagNET_DVR_MATRIX_LOGO_CFG
