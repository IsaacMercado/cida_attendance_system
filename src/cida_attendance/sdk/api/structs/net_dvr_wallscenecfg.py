from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_WALLSCENECFG(Structure):
    pass

_S(struct_tagNET_DVR_WALLSCENECFG, [
    ('dwSize', DWORD),
    ('sSceneName', BYTE * 32),
    ('byEnable', BYTE),
    ('bySceneIndex', BYTE),
    ('byRes', BYTE * 78),
])

NET_DVR_WALLSCENECFG = struct_tagNET_DVR_WALLSCENECFG
LPNET_DVR_WALLSCENECFG = POINTER(struct_tagNET_DVR_WALLSCENECFG)
tagNET_DVR_WALLSCENECFG = struct_tagNET_DVR_WALLSCENECFG
