from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_vca_rect import NET_VCA_RECT


class struct_tagNET_DVR_ROI_FIX_RECT_CFG(Structure):
    pass

_S(struct_tagNET_DVR_ROI_FIX_RECT_CFG, [
    ('byEnableFixRoi', BYTE),
    ('byImageQualityLevel', BYTE),
    ('byRes', BYTE * 2),
    ('szFixRoiName', BYTE * 32),
    ('struRoiRect', NET_VCA_RECT),
    ('byRes1', BYTE * 468),
])

NET_DVR_ROI_FIX_RECT_CFG = struct_tagNET_DVR_ROI_FIX_RECT_CFG
LPNET_DVR_ROI_FIX_RECT_CFG = POINTER(struct_tagNET_DVR_ROI_FIX_RECT_CFG)
tagNET_DVR_ROI_FIX_RECT_CFG = struct_tagNET_DVR_ROI_FIX_RECT_CFG
