from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, LONG
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SCENE_COND(Structure):
    pass

_S(struct_tagNET_DVR_SCENE_COND, [
    ('dwSize', DWORD),
    ('lChannel', LONG),
    ('dwSceneID', DWORD),
    ('byRes', BYTE * 48),
])

NET_DVR_SCENE_COND = struct_tagNET_DVR_SCENE_COND
LPNET_DVR_SCENE_COND = POINTER(struct_tagNET_DVR_SCENE_COND)
tagNET_DVR_SCENE_COND = struct_tagNET_DVR_SCENE_COND
