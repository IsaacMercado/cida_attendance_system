from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_bigscreencfg import NET_DVR_BIGSCREENCFG
from .net_dvr_wincfg import NET_DVR_WINCFG


class struct_tagNET_DVR_BIGSCREENCFG_SCENE(Structure):
    pass

_S(struct_tagNET_DVR_BIGSCREENCFG_SCENE, [
    ('byAllValid', BYTE),
    ('byAssociateBaseMap', BYTE),
    ('byEnableSpartan', BYTE),
    ('byRes', BYTE),
    ('struWinCfg', NET_DVR_WINCFG * 32),
    ('struBigScreen', NET_DVR_BIGSCREENCFG),
])

NET_DVR_BIGSCREENCFG_SCENE = struct_tagNET_DVR_BIGSCREENCFG_SCENE
LPNET_DVR_BIGSCREENCFG_SCENE = POINTER(struct_tagNET_DVR_BIGSCREENCFG_SCENE)
tagNET_DVR_BIGSCREENCFG_SCENE = struct_tagNET_DVR_BIGSCREENCFG_SCENE
