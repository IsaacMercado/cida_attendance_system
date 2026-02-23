from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_roi_detect_union import NET_DVR_ROI_DETECT_UNION


class struct_tagNET_DVR_ROI_DETECT_CFG(Structure):
    pass

_S(struct_tagNET_DVR_ROI_DETECT_CFG, [
    ('dwSize', DWORD),
    ('dwStreamType', DWORD),
    ('byRoiDetectType', BYTE),
    ('byRes', BYTE * 3),
    ('uRoiDetectInfo', NET_DVR_ROI_DETECT_UNION),
    ('byRes1', BYTE * 36),
])

NET_DVR_ROI_DETECT_CFG = struct_tagNET_DVR_ROI_DETECT_CFG
LPNET_DVR_ROI_DETECT_CFG = POINTER(struct_tagNET_DVR_ROI_DETECT_CFG)
tagNET_DVR_ROI_DETECT_CFG = struct_tagNET_DVR_ROI_DETECT_CFG
