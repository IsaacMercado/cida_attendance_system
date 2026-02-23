from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_NAKED_DATA_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_NAKED_DATA_PARAM, [
    ('wPort', WORD),
    ('byRes', BYTE * 130),
])

NET_DVR_NAKED_DATA_PARAM = struct_tagNET_DVR_NAKED_DATA_PARAM
LPNET_DVR_NAKED_DATA_PARAM = POINTER(struct_tagNET_DVR_NAKED_DATA_PARAM)
tagNET_DVR_NAKED_DATA_PARAM = struct_tagNET_DVR_NAKED_DATA_PARAM
