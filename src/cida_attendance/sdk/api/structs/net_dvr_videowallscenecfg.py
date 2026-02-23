from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_VIDEOWALLSCENECFG(Structure):
    pass

_S(struct_tagNET_DVR_VIDEOWALLSCENECFG, [
    ('dwSize', DWORD),
    ('sSceneName', BYTE * 32),
    ('byEnable', BYTE),
    ('bySceneIndex', BYTE),
    ('byRes', BYTE * 78),
])

NET_DVR_VIDEOWALLSCENECFG = struct_tagNET_DVR_VIDEOWALLSCENECFG
LPNET_DVR_VIDEOWALLSCENECFG = POINTER(struct_tagNET_DVR_VIDEOWALLSCENECFG)
tagNET_DVR_VIDEOWALLSCENECFG = struct_tagNET_DVR_VIDEOWALLSCENECFG
