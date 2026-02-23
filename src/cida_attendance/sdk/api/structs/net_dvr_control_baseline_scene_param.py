from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CONTROL_BASELINE_SCENE_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_CONTROL_BASELINE_SCENE_PARAM, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('byCommand', BYTE),
    ('byRes', BYTE * 127),
])

NET_DVR_CONTROL_BASELINE_SCENE_PARAM = struct_tagNET_DVR_CONTROL_BASELINE_SCENE_PARAM
LPNET_DVR_CONTROL_BASELINE_SCENE_PARAM = POINTER(struct_tagNET_DVR_CONTROL_BASELINE_SCENE_PARAM)
tagNET_DVR_CONTROL_BASELINE_SCENE_PARAM = struct_tagNET_DVR_CONTROL_BASELINE_SCENE_PARAM
