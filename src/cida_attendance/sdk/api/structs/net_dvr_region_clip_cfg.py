from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_vca_polygon import NET_VCA_POLYGON


class struct_tagNET_DVR_REGION_CLIP_CFG(Structure):
    pass

_S(struct_tagNET_DVR_REGION_CLIP_CFG, [
    ('dwSize', DWORD),
    ('byEnabled', BYTE),
    ('byRes1', BYTE * 3),
    ('wResolutionWidth', WORD),
    ('wResolutionHeight', WORD),
    ('struRegion', NET_VCA_POLYGON * 8),
    ('byRes2', BYTE * 64),
])

NET_DVR_REGION_CLIP_CFG = struct_tagNET_DVR_REGION_CLIP_CFG
LPNET_DVR_REGION_CLIP_CFG = POINTER(struct_tagNET_DVR_REGION_CLIP_CFG)
tagNET_DVR_REGION_CLIP_CFG = struct_tagNET_DVR_REGION_CLIP_CFG
