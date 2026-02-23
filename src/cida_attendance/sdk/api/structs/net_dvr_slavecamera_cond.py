from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SLAVECAMERA_COND(Structure):
    pass

_S(struct_tagNET_DVR_SLAVECAMERA_COND, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('byID', BYTE),
    ('byRes1', BYTE * 3),
    ('dwSceneID', DWORD),
    ('byRes', BYTE * 56),
])

NET_DVR_SLAVECAMERA_COND = struct_tagNET_DVR_SLAVECAMERA_COND
LPNET_DVR_SLAVECAMERA_COND = POINTER(struct_tagNET_DVR_SLAVECAMERA_COND)
tagNET_DVR_SLAVECAMERA_COND = struct_tagNET_DVR_SLAVECAMERA_COND
