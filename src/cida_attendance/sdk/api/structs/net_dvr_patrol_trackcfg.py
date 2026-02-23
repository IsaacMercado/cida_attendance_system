from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_patrol_scene_info import NET_DVR_PATROL_SCENE_INFO


class struct_tagNET_DVR_PATROL_TRACKCFG(Structure):
    pass

_S(struct_tagNET_DVR_PATROL_TRACKCFG, [
    ('dwSize', DWORD),
    ('struPatrolSceneInfo', NET_DVR_PATROL_SCENE_INFO * 10),
    ('byRes', BYTE * 16),
])

NET_DVR_PATROL_TRACKCFG = struct_tagNET_DVR_PATROL_TRACKCFG
LPNET_DVR_PATROL_TRACKCFG = POINTER(struct_tagNET_DVR_PATROL_TRACKCFG)
tagNET_DVR_PATROL_TRACKCFG = struct_tagNET_DVR_PATROL_TRACKCFG
