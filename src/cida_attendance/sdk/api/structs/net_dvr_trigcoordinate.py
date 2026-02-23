from ctypes import Structure

from ..base_classes import _S, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_TRIGCOORDINATE(Structure):
    pass

_S(struct_tagNET_DVR_TRIGCOORDINATE, [
    ('wTopLeftX', WORD),
    ('wTopLeftY', WORD),
    ('wWdith', WORD),
    ('wHeight', WORD),
])

NET_DVR_TRIGCOORDINATE = struct_tagNET_DVR_TRIGCOORDINATE
LPNET_DVR_TRIGCOORDINATE = POINTER(struct_tagNET_DVR_TRIGCOORDINATE)
tagNET_DVR_TRIGCOORDINATE = struct_tagNET_DVR_TRIGCOORDINATE
