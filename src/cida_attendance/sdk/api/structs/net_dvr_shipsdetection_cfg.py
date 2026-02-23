from ctypes import Structure, c_float

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_shipsdetection_region_cfg import NET_DVR_SHIPSDETECTION_REGION_CFG


class struct_tagNET_DVR_SHIPSDETECTION_CFG(Structure):
    pass

_S(struct_tagNET_DVR_SHIPSDETECTION_CFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byRes1', BYTE * 3),
    ('fLookDownUpAngle', c_float),
    ('fHorizontalHeight', c_float),
    ('struShipsDetectionRegion', NET_DVR_SHIPSDETECTION_REGION_CFG * 8),
    ('byRes', BYTE * 256),
])

NET_DVR_SHIPSDETECTION_CFG = struct_tagNET_DVR_SHIPSDETECTION_CFG
LPNET_DVR_SHIPSDETECTION_CFG = POINTER(struct_tagNET_DVR_SHIPSDETECTION_CFG)
tagNET_DVR_SHIPSDETECTION_CFG = struct_tagNET_DVR_SHIPSDETECTION_CFG
