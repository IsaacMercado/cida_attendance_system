from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_rectcfg_ex import NET_DVR_RECTCFG_EX


class struct_tagNET_DVR_VIDEOWALLDISPLAYMODE(Structure):
    pass

_S(struct_tagNET_DVR_VIDEOWALLDISPLAYMODE, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byRes1', BYTE * 3),
    ('struRect', NET_DVR_RECTCFG_EX),
    ('sName', BYTE * 32),
    ('byRes2', BYTE * 100),
])

NET_DVR_VIDEOWALLDISPLAYMODE = struct_tagNET_DVR_VIDEOWALLDISPLAYMODE
LPNET_DVR_VIDEOWALLDISPLAYMODE = POINTER(struct_tagNET_DVR_VIDEOWALLDISPLAYMODE)
tagNET_DVR_VIDEOWALLDISPLAYMODE = struct_tagNET_DVR_VIDEOWALLDISPLAYMODE
