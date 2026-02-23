from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_video_wall_info import NET_DVR_VIDEO_WALL_INFO


class struct_tagNET_DVR_SCENE_CONTROL_INFO(Structure):
    pass

_S(struct_tagNET_DVR_SCENE_CONTROL_INFO, [
    ('dwSize', DWORD),
    ('struVideoWallInfo', NET_DVR_VIDEO_WALL_INFO),
    ('dwCmd', DWORD),
    ('byRes', BYTE * 4),
])

NET_DVR_SCENE_CONTROL_INFO = struct_tagNET_DVR_SCENE_CONTROL_INFO
LPNET_DVR_SCENE_CONTROL_INFO = POINTER(struct_tagNET_DVR_SCENE_CONTROL_INFO)
tagNET_DVR_SCENE_CONTROL_INFO = struct_tagNET_DVR_SCENE_CONTROL_INFO
