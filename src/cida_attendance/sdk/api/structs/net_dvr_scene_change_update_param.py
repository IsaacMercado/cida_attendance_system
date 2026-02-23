from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SCENE_CHANGE_UPDATE_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_SCENE_CHANGE_UPDATE_PARAM, [
    ('dwSize', DWORD),
    ('byIDCount', BYTE),
    ('byRes1', BYTE * 3),
    ('byStreamID', (BYTE * 32) * 30),
    ('byRes', BYTE * 256),
])

NET_DVR_SCENE_CHANGE_UPDATE_PARAM = struct_tagNET_DVR_SCENE_CHANGE_UPDATE_PARAM
LPNET_DVR_SCENE_CHANGE_UPDATE_PARAM = POINTER(struct_tagNET_DVR_SCENE_CHANGE_UPDATE_PARAM)
tagNET_DVR_SCENE_CHANGE_UPDATE_PARAM = struct_tagNET_DVR_SCENE_CHANGE_UPDATE_PARAM
