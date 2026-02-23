from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_rect import NET_VCA_RECT


class struct_tagNET_DVR_AREA_MASK_CFG(Structure):
    pass

_S(struct_tagNET_DVR_AREA_MASK_CFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byMaskThick', BYTE),
    ('byAutoMask', BYTE),
    ('byRes1', BYTE),
    ('struRegion', NET_VCA_RECT * 8),
    ('byRes', BYTE * 64),
])

NET_DVR_AREA_MASK_CFG = struct_tagNET_DVR_AREA_MASK_CFG
LPNET_DVR_AREA_MASK_CFG = POINTER(struct_tagNET_DVR_AREA_MASK_CFG)
tagNET_DVR_AREA_MASK_CFG = struct_tagNET_DVR_AREA_MASK_CFG
