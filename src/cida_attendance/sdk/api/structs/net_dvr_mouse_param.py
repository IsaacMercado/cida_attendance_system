from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_screen_point import NET_DVR_SCREEN_POINT


class struct_tagNET_DVR_MOUSE_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_MOUSE_PARAM, [
    ('byMouseEvent', BYTE),
    ('byRes1', BYTE * 3),
    ('struMousePoint', NET_DVR_SCREEN_POINT),
    ('byRes2', BYTE * 8),
])

NET_DVR_MOUSE_PARAM = struct_tagNET_DVR_MOUSE_PARAM
LPNET_DVR_MOUSE_PARAM = POINTER(struct_tagNET_DVR_MOUSE_PARAM)
tagNET_DVR_MOUSE_PARAM = struct_tagNET_DVR_MOUSE_PARAM
