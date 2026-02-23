from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_screen_point import NET_DVR_SCREEN_POINT


class struct_tagNET_DVR_PPT_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_PPT_PARAM, [
    ('byPPTAction', BYTE),
    ('byRes1', BYTE * 3),
    ('struPoint', NET_DVR_SCREEN_POINT),
    ('dwPPTNo', DWORD),
    ('byRes2', BYTE * 4),
])

NET_DVR_PPT_PARAM = struct_tagNET_DVR_PPT_PARAM
LPNET_DVR_PPT_PARAM = POINTER(struct_tagNET_DVR_PPT_PARAM)
tagNET_DVR_PPT_PARAM = struct_tagNET_DVR_PPT_PARAM
