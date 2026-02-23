from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_rectcfg_ex import NET_DVR_RECTCFG_EX


class struct_tagNET_DVR_VIDEOWALLDISPLAYPOSITION(Structure):
    pass

_S(struct_tagNET_DVR_VIDEOWALLDISPLAYPOSITION, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byCoordinateType', BYTE),
    ('byRes1', BYTE * 2),
    ('dwVideoWallNo', DWORD),
    ('dwDisplayNo', DWORD),
    ('struRectCfg', NET_DVR_RECTCFG_EX),
    ('byRes2', BYTE * 64),
])

NET_DVR_VIDEOWALLDISPLAYPOSITION = struct_tagNET_DVR_VIDEOWALLDISPLAYPOSITION
LPNET_DVR_VIDEOWALLDISPLAYPOSITION = POINTER(struct_tagNET_DVR_VIDEOWALLDISPLAYPOSITION)
tagNET_DVR_VIDEOWALLDISPLAYPOSITION = struct_tagNET_DVR_VIDEOWALLDISPLAYPOSITION
