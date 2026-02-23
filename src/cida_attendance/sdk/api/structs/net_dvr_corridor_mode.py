from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CORRIDOR_MODE(Structure):
    pass

_S(struct_tagNET_DVR_CORRIDOR_MODE, [
    ('dwSize', DWORD),
    ('byEnableCorridorMode', BYTE),
    ('byMirrorMode', BYTE),
    ('byRes', BYTE * 126),
])

NET_DVR_CORRIDOR_MODE = struct_tagNET_DVR_CORRIDOR_MODE
LPNET_DVR_CORRIDOR_MODE = POINTER(struct_tagNET_DVR_CORRIDOR_MODE)
tagNET_DVR_CORRIDOR_MODE = struct_tagNET_DVR_CORRIDOR_MODE
