from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_rectcfg import NET_DVR_RECTCFG


class struct_tagNET_DVR_SCREEN_WINCFG(Structure):
    pass

_S(struct_tagNET_DVR_SCREEN_WINCFG, [
    ('dwSize', DWORD),
    ('byVaild', BYTE),
    ('byInputType', BYTE),
    ('wInputIdx', WORD),
    ('dwLayerIdx', DWORD),
    ('struWin', NET_DVR_RECTCFG),
    ('byWndIndex', BYTE),
    ('byCBD', BYTE),
    ('bySubWnd', BYTE),
    ('byRes1', BYTE),
    ('dwDeviceIndex', DWORD),
    ('byRes2', BYTE * 16),
])

NET_DVR_SCREEN_WINCFG = struct_tagNET_DVR_SCREEN_WINCFG
LPNET_DVR_SCREEN_WINCFG = POINTER(struct_tagNET_DVR_SCREEN_WINCFG)
tagNET_DVR_SCREEN_WINCFG = struct_tagNET_DVR_SCREEN_WINCFG
