from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_OSD_POSITION(Structure):
    pass

_S(struct_tagNET_DVR_OSD_POSITION, [
    ('byPositionMode', BYTE),
    ('byRes1', BYTE * 3),
    ('dwPosX', DWORD),
    ('dwPosY', DWORD),
    ('byRes2', BYTE * 8),
])

NET_DVR_OSD_POSITION = struct_tagNET_DVR_OSD_POSITION
LPNET_DVR_OSD_POSITION = POINTER(struct_tagNET_DVR_OSD_POSITION)
tagNET_DVR_OSD_POSITION = struct_tagNET_DVR_OSD_POSITION
