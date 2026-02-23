from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_itc_polygon import NET_ITC_POLYGON
from .net_vca_line import NET_VCA_LINE


class struct_tagNET_DVR_SHIPSDETECTION_REGION_CFG(Structure):
    pass

_S(struct_tagNET_DVR_SHIPSDETECTION_REGION_CFG, [
    ('byRuleID', BYTE),
    ('byEnable', BYTE),
    ('bySensitivity', BYTE),
    ('byFrameOverlayEnabled', BYTE),
    ('byRes', BYTE * 36),
    ('struPolygon', NET_ITC_POLYGON),
    ('struTriggerLine', NET_VCA_LINE),
])

NET_DVR_SHIPSDETECTION_REGION_CFG = struct_tagNET_DVR_SHIPSDETECTION_REGION_CFG
LPNET_DVR_SHIPSDETECTION_REGION_CFG = POINTER(struct_tagNET_DVR_SHIPSDETECTION_REGION_CFG)
tagNET_DVR_SHIPSDETECTION_REGION_CFG = struct_tagNET_DVR_SHIPSDETECTION_REGION_CFG
