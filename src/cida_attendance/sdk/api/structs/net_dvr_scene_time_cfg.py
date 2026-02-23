from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_one_scene_time import NET_DVR_ONE_SCENE_TIME


class struct_tagNET_DVR_SCENE_TIME_CFG(Structure):
    pass

_S(struct_tagNET_DVR_SCENE_TIME_CFG, [
    ('dwSize', DWORD),
    ('struSceneTime', NET_DVR_ONE_SCENE_TIME * 16),
    ('byRes', BYTE * 64),
])

NET_DVR_SCENE_TIME_CFG = struct_tagNET_DVR_SCENE_TIME_CFG
LPNET_DVR_SCENE_TIME_CFG = POINTER(struct_tagNET_DVR_SCENE_TIME_CFG)
tagNET_DVR_SCENE_TIME_CFG = struct_tagNET_DVR_SCENE_TIME_CFG
