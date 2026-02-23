from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_6 import NET_DVR_SCHEDTIME


class struct_tagNET_DVR_ONE_SCENE_TIME(Structure):
    pass

_S(struct_tagNET_DVR_ONE_SCENE_TIME, [
    ('byActive', BYTE),
    ('byRes1', BYTE * 3),
    ('dwSceneID', DWORD),
    ('struEffectiveTime', NET_DVR_SCHEDTIME),
    ('byRes2', BYTE * 16),
])

NET_DVR_ONE_SCENE_TIME = struct_tagNET_DVR_ONE_SCENE_TIME
LPNET_DVR_ONE_SCENE_TIME = POINTER(struct_tagNET_DVR_ONE_SCENE_TIME)
tagNET_DVR_ONE_SCENE_TIME = struct_tagNET_DVR_ONE_SCENE_TIME
