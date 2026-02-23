from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PTZ_PRIORITIZECFG(Structure):
    pass

_S(struct_tagNET_DVR_PTZ_PRIORITIZECFG, [
    ('dwSize', DWORD),
    ('byPTZPrioritize', BYTE),
    ('byRes', BYTE * 3),
    ('dwDelay', DWORD),
    ('byRes1', BYTE * 124),
])

NET_DVR_PTZ_PRIORITIZECFG = struct_tagNET_DVR_PTZ_PRIORITIZECFG
LPNET_DVR_PTZ_PRIORITIZECFG = POINTER(struct_tagNET_DVR_PTZ_PRIORITIZECFG)
tagNET_DVR_PTZ_PRIORITIZECFG = struct_tagNET_DVR_PTZ_PRIORITIZECFG
