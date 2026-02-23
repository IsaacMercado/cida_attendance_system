from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_rectcfg_ex import NET_DVR_RECTCFG_EX


class struct_tagNET_DVR_VIDEO_WALL_AREA(Structure):
    pass

_S(struct_tagNET_DVR_VIDEO_WALL_AREA, [
    ('dwSize', DWORD),
    ('byWallNo', BYTE),
    ('byRes1', BYTE * 3),
    ('struRect', NET_DVR_RECTCFG_EX),
    ('byRes2', BYTE * 32),
])

NET_DVR_VIDEO_WALL_AREA = struct_tagNET_DVR_VIDEO_WALL_AREA
LPNET_DVR_VIDEO_WALL_AREA = POINTER(struct_tagNET_DVR_VIDEO_WALL_AREA)
tagNET_DVR_VIDEO_WALL_AREA = struct_tagNET_DVR_VIDEO_WALL_AREA
