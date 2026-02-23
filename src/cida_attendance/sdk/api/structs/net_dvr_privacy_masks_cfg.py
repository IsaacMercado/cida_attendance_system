from ctypes import Structure, c_char, c_float

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_polygon import NET_VCA_POLYGON


class struct_tagNET_DVR_PRIVACY_MASKS_CFG(Structure):
    pass

_S(struct_tagNET_DVR_PRIVACY_MASKS_CFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byPrivacyMaskCfgEnable', BYTE),
    ('byColorType', BYTE),
    ('byActiveZoomRatio', BYTE),
    ('sPrivacyMaskName', c_char * 32),
    ('struRegion', NET_VCA_POLYGON),
    ('byCurrentRegionEnable', BYTE),
    ('byCurZoomRatio', BYTE),
    ('byRes', BYTE * 2),
    ('fActiveZoomRatio', c_float),
    ('byRes1', BYTE * 120),
])

NET_DVR_PRIVACY_MASKS_CFG = struct_tagNET_DVR_PRIVACY_MASKS_CFG
LPNET_DVR_PRIVACY_MASKS_CFG = POINTER(struct_tagNET_DVR_PRIVACY_MASKS_CFG)
tagNET_DVR_PRIVACY_MASKS_CFG = struct_tagNET_DVR_PRIVACY_MASKS_CFG
