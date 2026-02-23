from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_VIDEO_WALL_INFO(Structure):
    pass

_S(struct_tagNET_DVR_VIDEO_WALL_INFO, [
    ('dwSize', DWORD),
    ('dwWindowNo', DWORD),
    ('dwSceneNo', DWORD),
    ('dwDestWallNo', DWORD),
    ('dwDestSceneNo', DWORD),
    ('byRes', BYTE * 12),
])

NET_DVR_VIDEO_WALL_INFO = struct_tagNET_DVR_VIDEO_WALL_INFO
LPNET_DVR_VIDEO_WALL_INFO = POINTER(struct_tagNET_DVR_VIDEO_WALL_INFO)
tagNET_DVR_VIDEO_WALL_INFO = struct_tagNET_DVR_VIDEO_WALL_INFO
