from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_wincfg import NET_DVR_WINCFG


class struct_tagNET_DVR_ALLWINCFG(Structure):
    pass

_S(struct_tagNET_DVR_ALLWINCFG, [
    ('dwSize', DWORD),
    ('struWinCfg', NET_DVR_WINCFG * 32),
    ('byRes2', BYTE * 24),
])

NET_DVR_ALLWINCFG = struct_tagNET_DVR_ALLWINCFG
LPNET_DVR_ALLWINCFG = POINTER(struct_tagNET_DVR_ALLWINCFG)
tagNET_DVR_ALLWINCFG = struct_tagNET_DVR_ALLWINCFG
