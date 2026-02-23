from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_polygon import NET_VCA_POLYGON


class struct_tagNET_DVR_IMAGE_DIFF_DETECTION_CFG(Structure):
    pass

_S(struct_tagNET_DVR_IMAGE_DIFF_DETECTION_CFG, [
    ('dwSize', DWORD),
    ('struRegion', NET_VCA_POLYGON),
    ('byEnabled', BYTE),
    ('byThreshold', BYTE),
    ('bySensitivity', BYTE),
    ('byVideoInputType', BYTE),
    ('byRes', BYTE * 300),
])

NET_DVR_IMAGE_DIFF_DETECTION_CFG = struct_tagNET_DVR_IMAGE_DIFF_DETECTION_CFG
LPNET_DVR_IMAGE_DIFF_DETECTION_CFG = POINTER(struct_tagNET_DVR_IMAGE_DIFF_DETECTION_CFG)
tagNET_DVR_IMAGE_DIFF_DETECTION_CFG = struct_tagNET_DVR_IMAGE_DIFF_DETECTION_CFG
