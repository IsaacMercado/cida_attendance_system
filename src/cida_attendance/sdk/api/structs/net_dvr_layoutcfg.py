from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_screen_wincfg import NET_DVR_SCREEN_WINCFG


class struct_tagNET_DVR_LAYOUTCFG(Structure):
    pass

_S(struct_tagNET_DVR_LAYOUTCFG, [
    ('dwSize', DWORD),
    ('byValid', BYTE),
    ('byRes1', BYTE * 3),
    ('byLayoutName', BYTE * 32),
    ('struWinCfg', NET_DVR_SCREEN_WINCFG * 224),
    ('byRes2', BYTE * 16),
])

NET_DVR_LAYOUTCFG = struct_tagNET_DVR_LAYOUTCFG
LPNET_DVR_LAYOUTCFG = POINTER(struct_tagNET_DVR_LAYOUTCFG)
tagNET_DVR_LAYOUTCFG = struct_tagNET_DVR_LAYOUTCFG
