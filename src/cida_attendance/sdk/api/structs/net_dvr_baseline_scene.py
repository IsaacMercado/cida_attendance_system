from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_BASELINE_SCENE(Structure):
    pass

_S(struct_tagNET_DVR_BASELINE_SCENE, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byRes', BYTE * 63),
])

NET_DVR_BASELINE_SCENE = struct_tagNET_DVR_BASELINE_SCENE
LPNET_DVR_BASELINE_SCENE = POINTER(struct_tagNET_DVR_BASELINE_SCENE)
tagNET_DVR_BASELINE_SCENE = struct_tagNET_DVR_BASELINE_SCENE
