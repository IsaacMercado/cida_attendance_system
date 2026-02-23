from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_POSITION_INDEX(Structure):
    pass

_S(struct_tagNET_DVR_POSITION_INDEX, [
    ('byIndex', BYTE),
    ('byRes1', BYTE),
    ('wDwell', WORD),
    ('byRes2', BYTE * 4),
])

NET_DVR_POSITION_INDEX = struct_tagNET_DVR_POSITION_INDEX
LPNET_DVR_POSITION_INDEX = POINTER(struct_tagNET_DVR_POSITION_INDEX)
tagNET_DVR_POSITION_INDEX = struct_tagNET_DVR_POSITION_INDEX
