from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_NAKED_DATA_INFO(Structure):
    pass

_S(struct_tagNET_DVR_NAKED_DATA_INFO, [
    ('sSocketIP', c_char * 128),
    ('wSocktPort', WORD),
    ('byRes', BYTE * 258),
])

NET_DVR_NAKED_DATA_INFO = struct_tagNET_DVR_NAKED_DATA_INFO
LPNET_DVR_NAKED_DATA_INFO = POINTER(struct_tagNET_DVR_NAKED_DATA_INFO)
tagNET_DVR_NAKED_DATA_INFO = struct_tagNET_DVR_NAKED_DATA_INFO
