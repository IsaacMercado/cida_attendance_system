from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_point import NET_VCA_POINT


class struct_tagNET_DVR_MOUSE_EVENT_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_MOUSE_EVENT_PARAM, [
    ('dwSize', DWORD),
    ('byMouseEvent', BYTE),
    ('byRes1', BYTE * 3),
    ('struPoint', NET_VCA_POINT),
    ('byRes', BYTE * 64),
])

NET_DVR_MOUSE_EVENT_PARAM = struct_tagNET_DVR_MOUSE_EVENT_PARAM
LPNET_DVR_MOUSE_EVENT_PARAM = POINTER(struct_tagNET_DVR_MOUSE_EVENT_PARAM)
tagNET_DVR_MOUSE_EVENT_PARAM = struct_tagNET_DVR_MOUSE_EVENT_PARAM
