from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_rectcfg import NET_DVR_RECTCFG


class struct_tagNET_DVR_WINCFG(Structure):
    pass

_S(struct_tagNET_DVR_WINCFG, [
    ('dwSize', DWORD),
    ('byVaild', BYTE),
    ('byInputIdx', BYTE),
    ('byLayerIdx', BYTE),
    ('byTransparency', BYTE),
    ('struWin', NET_DVR_RECTCFG),
    ('wScreenHeight', WORD),
    ('wScreenWidth', WORD),
    ('byRes', BYTE * 20),
])

NET_DVR_WINCFG = struct_tagNET_DVR_WINCFG
LPNET_DVR_WINCFG = POINTER(struct_tagNET_DVR_WINCFG)
tagNET_DVR_WINCFG = struct_tagNET_DVR_WINCFG
