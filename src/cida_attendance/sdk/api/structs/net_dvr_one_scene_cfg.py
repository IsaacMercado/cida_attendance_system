from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_186 import NET_DVR_PTZPOS


class struct_tagNET_DVR_ONE_SCENE_CFG_(Structure):
    pass

_S(struct_tagNET_DVR_ONE_SCENE_CFG_, [
    ('byEnable', BYTE),
    ('byDirection', BYTE),
    ('byRes1', BYTE * 2),
    ('dwSceneID', DWORD),
    ('bySceneName', BYTE * 32),
    ('struPtzPos', NET_DVR_PTZPOS),
    ('dwTrackTime', DWORD),
    ('byRes2', BYTE * 24),
])

NET_DVR_ONE_SCENE_CFG = struct_tagNET_DVR_ONE_SCENE_CFG_
LPNET_DVR_ONE_SCENE_CFG = POINTER(struct_tagNET_DVR_ONE_SCENE_CFG_)
tagNET_DVR_ONE_SCENE_CFG_ = struct_tagNET_DVR_ONE_SCENE_CFG_
