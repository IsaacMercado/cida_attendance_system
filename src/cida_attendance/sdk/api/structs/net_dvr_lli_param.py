from ctypes import Structure, c_float

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_LLI_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_LLI_PARAM, [
    ('fSec', c_float),
    ('byDegree', BYTE),
    ('byMinute', BYTE),
    ('byRes', BYTE * 6),
])

NET_DVR_LLI_PARAM = struct_tagNET_DVR_LLI_PARAM
LPNET_DVR_LLI_PARAM = POINTER(struct_tagNET_DVR_LLI_PARAM)
tagNET_DVR_LLI_PARAM = struct_tagNET_DVR_LLI_PARAM
