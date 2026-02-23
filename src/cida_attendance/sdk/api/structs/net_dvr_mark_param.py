from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_27 import NET_DVR_RGB_COLOR
from .net_dvr_screen_point import NET_DVR_SCREEN_POINT


class struct_tagNET_DVR_MARK_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_MARK_PARAM, [
    ('byMarkEvent', BYTE),
    ('byMarkTool', BYTE),
    ('byLineWidth', BYTE),
    ('byMouseEvent', BYTE),
    ('struColor', NET_DVR_RGB_COLOR),
    ('struPoint', NET_DVR_SCREEN_POINT),
    ('byRes', BYTE * 4),
])

NET_DVR_MARK_PARAM = struct_tagNET_DVR_MARK_PARAM
LPNET_DVR_MARK_PARAM = POINTER(struct_tagNET_DVR_MARK_PARAM)
tagNET_DVR_MARK_PARAM = struct_tagNET_DVR_MARK_PARAM
