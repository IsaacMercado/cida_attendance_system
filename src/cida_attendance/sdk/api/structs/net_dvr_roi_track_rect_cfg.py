from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ROI_TRACK_RECT_CFG(Structure):
    pass

_S(struct_tagNET_DVR_ROI_TRACK_RECT_CFG, [
    ('byEnableTrackRoi', BYTE),
    ('byImageQualityLevel', BYTE),
    ('byModeType', BYTE),
    ('byRes', BYTE * 509),
])

NET_DVR_ROI_TRACK_RECT_CFG = struct_tagNET_DVR_ROI_TRACK_RECT_CFG
LPNET_DVR_ROI_TRACK_RECT_CFG = POINTER(struct_tagNET_DVR_ROI_TRACK_RECT_CFG)
tagNET_DVR_ROI_TRACK_RECT_CFG = struct_tagNET_DVR_ROI_TRACK_RECT_CFG
