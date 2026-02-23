from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_one_scene_cfg import NET_DVR_ONE_SCENE_CFG


class struct_tagNET_DVR_SCENE_CFG(Structure):
    pass

_S(struct_tagNET_DVR_SCENE_CFG, [
    ('dwSize', DWORD),
    ('struSceneCfg', NET_DVR_ONE_SCENE_CFG * 16),
    ('byRes', BYTE * 40),
])

NET_DVR_SCENE_CFG = struct_tagNET_DVR_SCENE_CFG
LPNET_DVR_SCENE_CFG = POINTER(struct_tagNET_DVR_SCENE_CFG)
tagNET_DVR_SCENE_CFG = struct_tagNET_DVR_SCENE_CFG
