from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_WALL_INDEX(Structure):
    pass

_S(struct_tagNET_DVR_WALL_INDEX, [
    ('dwSize', DWORD),
    ('byWallNo', BYTE),
    ('bySceneNo', BYTE),
    ('byRes1', BYTE * 2),
    ('dwDeviceID', DWORD),
    ('dwWindowNo', DWORD),
    ('byRes2', BYTE * 32),
])

NET_DVR_WALL_INDEX = struct_tagNET_DVR_WALL_INDEX
LPNET_DVR_WALL_INDEX = POINTER(struct_tagNET_DVR_WALL_INDEX)
tagNET_DVR_WALL_INDEX = struct_tagNET_DVR_WALL_INDEX
