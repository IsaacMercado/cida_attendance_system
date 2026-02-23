from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_rectcfg import NET_DVR_RECTCFG


class struct_tagNET_DVR_WALLWINCFG(Structure):
    pass

_S(struct_tagNET_DVR_WALLWINCFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byRes1', BYTE * 7),
    ('dwWinNum', DWORD),
    ('dwLayerIndex', DWORD),
    ('struWinPosition', NET_DVR_RECTCFG),
    ('dwDeviceIndex', DWORD),
    ('wInputIndex', WORD),
    ('byRes2', BYTE * 14),
])

NET_DVR_WALLWINCFG = struct_tagNET_DVR_WALLWINCFG
LPNET_DVR_WALLWINCFG = POINTER(struct_tagNET_DVR_WALLWINCFG)
tagNET_DVR_WALLWINCFG = struct_tagNET_DVR_WALLWINCFG
