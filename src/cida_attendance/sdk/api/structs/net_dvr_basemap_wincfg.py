from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_rectcfg_ex import NET_DVR_RECTCFG_EX


class struct_tagNET_DVR_BASEMAP_WINCFG(Structure):
    pass

_S(struct_tagNET_DVR_BASEMAP_WINCFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byWndOperateMode', BYTE),
    ('byRes1', BYTE * 6),
    ('struWinPosition', NET_DVR_RECTCFG_EX),
    ('struResolution', NET_DVR_RECTCFG_EX),
    ('dwXCoordinate', DWORD),
    ('dwYCoordinate', DWORD),
    ('byRes2', BYTE * 36),
])

NET_DVR_BASEMAP_WINCFG = struct_tagNET_DVR_BASEMAP_WINCFG
LPNET_DVR_BASEMAP_WINCFG = POINTER(struct_tagNET_DVR_BASEMAP_WINCFG)
tagNET_DVR_BASEMAP_WINCFG = struct_tagNET_DVR_BASEMAP_WINCFG
