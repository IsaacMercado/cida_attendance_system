from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_rectcfg import NET_DVR_RECTCFG


class struct_tagNET_DVR_SINGLEWALLPARAM(Structure):
    pass

_S(struct_tagNET_DVR_SINGLEWALLPARAM, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byRes1', BYTE * 3),
    ('dwWallNum', DWORD),
    ('struRectCfg', NET_DVR_RECTCFG),
    ('byRes2', BYTE * 36),
])

NET_DVR_SINGLEWALLPARAM = struct_tagNET_DVR_SINGLEWALLPARAM
LPNET_DVR_SINGLEWALLPARAM = POINTER(struct_tagNET_DVR_SINGLEWALLPARAM)
tagNET_DVR_SINGLEWALLPARAM = struct_tagNET_DVR_SINGLEWALLPARAM
