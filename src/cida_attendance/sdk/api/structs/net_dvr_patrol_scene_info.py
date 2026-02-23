from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PATROL_SCENE_INFO(Structure):
    pass

_S(struct_tagNET_DVR_PATROL_SCENE_INFO, [
    ('wDwell', WORD),
    ('byPositionID', BYTE),
    ('byRes', BYTE * 5),
])

NET_DVR_PATROL_SCENE_INFO = struct_tagNET_DVR_PATROL_SCENE_INFO
LPNET_DVR_PATROL_SCENE_INFO = POINTER(struct_tagNET_DVR_PATROL_SCENE_INFO)
tagNET_DVR_PATROL_SCENE_INFO = struct_tagNET_DVR_PATROL_SCENE_INFO
