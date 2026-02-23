from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_THERMINTELL_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_THERMINTELL_PARAM, [
    ('dwSize', DWORD),
    ('byIntellType', BYTE),
    ('byRes', BYTE * 127),
])

NET_DVR_THERMINTELL_PARAM = struct_tagNET_DVR_THERMINTELL_PARAM
LPNET_DVR_THERMINTELL_PARAM = POINTER(struct_tagNET_DVR_THERMINTELL_PARAM)
tagNET_DVR_THERMINTELL_PARAM = struct_tagNET_DVR_THERMINTELL_PARAM
