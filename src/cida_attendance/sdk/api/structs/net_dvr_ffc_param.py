from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_FFC_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_FFC_PARAM, [
    ('byMode', BYTE),
    ('byRes1', BYTE),
    ('wCompensateTime', WORD),
    ('byRes2', BYTE * 4),
])

NET_DVR_FFC_PARAM = struct_tagNET_DVR_FFC_PARAM
LPNET_DVR_FFC_PARAM = POINTER(struct_tagNET_DVR_FFC_PARAM)
tagNET_DVR_FFC_PARAM = struct_tagNET_DVR_FFC_PARAM
