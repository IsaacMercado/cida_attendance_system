from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_screen_point import NET_DVR_SCREEN_POINT


class struct_tagNET_DVR_SPOTLIGHT_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_SPOTLIGHT_PARAM, [
    ('byCmd', BYTE),
    ('byRes1', BYTE * 3),
    ('struPoint', NET_DVR_SCREEN_POINT),
    ('dwRadius', DWORD),
    ('byRes2', BYTE * 4),
])

NET_DVR_SPOTLIGHT_PARAM = struct_tagNET_DVR_SPOTLIGHT_PARAM
LPNET_DVR_SPOTLIGHT_PARAM = POINTER(struct_tagNET_DVR_SPOTLIGHT_PARAM)
tagNET_DVR_SPOTLIGHT_PARAM = struct_tagNET_DVR_SPOTLIGHT_PARAM
