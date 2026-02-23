from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_FOCUSING_POSITION_STATE(Structure):
    pass

_S(struct_tagNET_DVR_FOCUSING_POSITION_STATE, [
    ('dwSize', DWORD),
    ('byState', BYTE),
    ('byRes', BYTE * 31),
])

NET_DVR_FOCUSING_POSITION_STATE = struct_tagNET_DVR_FOCUSING_POSITION_STATE
LPNET_DVR_FOCUSING_POSITION_STATE = POINTER(struct_tagNET_DVR_FOCUSING_POSITION_STATE)
tagNET_DVR_FOCUSING_POSITION_STATE = struct_tagNET_DVR_FOCUSING_POSITION_STATE
