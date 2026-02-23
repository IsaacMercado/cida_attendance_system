from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_TRUNK_USE_STATE(Structure):
    pass

_S(struct_tagNET_DVR_TRUNK_USE_STATE, [
    ('dwSize', DWORD),
    ('dwTrunkID', DWORD),
    ('wReserveUserID', WORD),
    ('byStatus', BYTE),
    ('byRes1', BYTE),
    ('byUserId', BYTE * 256),
    ('byRes2', BYTE * 64),
])

NET_DVR_TRUNK_USE_STATE = struct_tagNET_DVR_TRUNK_USE_STATE
LPNET_DVR_TRUNK_USE_STATE = POINTER(struct_tagNET_DVR_TRUNK_USE_STATE)
tagNET_DVR_TRUNK_USE_STATE = struct_tagNET_DVR_TRUNK_USE_STATE
