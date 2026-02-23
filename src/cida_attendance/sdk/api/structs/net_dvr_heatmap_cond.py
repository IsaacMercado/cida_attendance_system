from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_HEATMAP_COND(Structure):
    pass

_S(struct_tagNET_DVR_HEATMAP_COND, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('byDetSceneID', BYTE),
    ('byRes', BYTE * 63),
])

NET_DVR_HEATMAP_COND = struct_tagNET_DVR_HEATMAP_COND
LPNET_DVR_HEATMAP_COND = POINTER(struct_tagNET_DVR_HEATMAP_COND)
tagNET_DVR_HEATMAP_COND = struct_tagNET_DVR_HEATMAP_COND
