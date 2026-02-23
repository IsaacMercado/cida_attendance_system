from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_rectcfg import NET_DVR_RECTCFG


class struct_tagNET_DVR_AREA_ZOOM_CFG(Structure):
    pass

_S(struct_tagNET_DVR_AREA_ZOOM_CFG, [
    ('byCmd', BYTE),
    ('byRes', BYTE * 3),
    ('struArea', NET_DVR_RECTCFG),
])

NET_DVR_AREA_ZOOM_CFG = struct_tagNET_DVR_AREA_ZOOM_CFG
LPNET_DVR_AREA_ZOOM_CFG = POINTER(struct_tagNET_DVR_AREA_ZOOM_CFG)
tagNET_DVR_AREA_ZOOM_CFG = struct_tagNET_DVR_AREA_ZOOM_CFG
