from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_GOTOSCENE_COND(Structure):
    pass

_S(struct_tagNET_DVR_GOTOSCENE_COND, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('dwSceneID', DWORD),
    ('byRes', BYTE * 512),
])

NET_DVR_GOTOSCENE_COND = struct_tagNET_DVR_GOTOSCENE_COND
LPNET_DVR_GOTOSCENE_COND = POINTER(struct_tagNET_DVR_GOTOSCENE_COND)
tagNET_DVR_GOTOSCENE_COND = struct_tagNET_DVR_GOTOSCENE_COND
