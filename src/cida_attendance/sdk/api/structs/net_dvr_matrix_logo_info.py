from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_MATRIX_LOGO_INFO(Structure):
    pass

_S(struct_tagNET_DVR_MATRIX_LOGO_INFO, [
    ('dwSize', DWORD),
    ('dwLogoSize', DWORD),
    ('byRes', BYTE * 32),
])

NET_DVR_MATRIX_LOGO_INFO = struct_tagNET_DVR_MATRIX_LOGO_INFO
LPNET_DVR_MATRIX_LOGO_INFO = POINTER(struct_tagNET_DVR_MATRIX_LOGO_INFO)
tagNET_DVR_MATRIX_LOGO_INFO = struct_tagNET_DVR_MATRIX_LOGO_INFO
