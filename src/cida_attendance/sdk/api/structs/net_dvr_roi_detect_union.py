from ctypes import Union

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_roi_fix_rect_cfg import NET_DVR_ROI_FIX_RECT_CFG
from .net_dvr_roi_track_rect_cfg import NET_DVR_ROI_TRACK_RECT_CFG


class union_tagNET_DVR_ROI_DETECT_UNION(Union):
    pass

_S(union_tagNET_DVR_ROI_DETECT_UNION, [
    ('uLen', DWORD * 128),
    ('strRoiFixRectCfg', NET_DVR_ROI_FIX_RECT_CFG),
    ('strRoiTrackRectCfg', NET_DVR_ROI_TRACK_RECT_CFG),
])

NET_DVR_ROI_DETECT_UNION = union_tagNET_DVR_ROI_DETECT_UNION
LPNET_DVR_ROI_DETECT_UNION = POINTER(union_tagNET_DVR_ROI_DETECT_UNION)
tagNET_DVR_ROI_DETECT_UNION = union_tagNET_DVR_ROI_DETECT_UNION
