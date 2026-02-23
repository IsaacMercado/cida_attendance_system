from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_186 import NET_DVR_PTZPOS


class struct_tagNET_DVR_SCENE_INFO_(Structure):
    pass

_S(struct_tagNET_DVR_SCENE_INFO_, [
    ('dwSceneID', DWORD),
    ('bySceneName', BYTE * 32),
    ('byDirection', BYTE),
    ('byRes1', BYTE * 3),
    ('struPtzPos', NET_DVR_PTZPOS),
    ('byRes2', BYTE * 64),
])

NET_DVR_SCENE_INFO = struct_tagNET_DVR_SCENE_INFO_
LPNET_DVR_SCENE_INFO = POINTER(struct_tagNET_DVR_SCENE_INFO_)
tagNET_DVR_SCENE_INFO_ = struct_tagNET_DVR_SCENE_INFO_
