from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_basemap_cfg import NET_DVR_BASEMAP_CFG


class struct_tagNET_DVR_PICCFG(Structure):
    pass

_S(struct_tagNET_DVR_PICCFG, [
    ('dwSize', DWORD),
    ('byUseType', BYTE),
    ('bySequence', BYTE),
    ('byOverlayEnabled', BYTE),
    ('byRes', BYTE * 1),
    ('struBasemapCfg', NET_DVR_BASEMAP_CFG),
    ('sPicName', BYTE * 32),
    ('dwVideoWall', DWORD),
    ('byFlash', BYTE),
    ('byTranslucent', BYTE),
    ('byShowEnabled', BYTE),
    ('byPictureType', BYTE),
    ('byRes2', BYTE * 24),
])

NET_DVR_PICTURECFG = struct_tagNET_DVR_PICCFG
LPNET_DVR_PICTURECFG = POINTER(struct_tagNET_DVR_PICCFG)
tagNET_DVR_PICCFG = struct_tagNET_DVR_PICCFG
