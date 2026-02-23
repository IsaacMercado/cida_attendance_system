from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_point import NET_VCA_POINT


class struct_tagNET_DVR_DRAG_POS_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_DRAG_POS_PARAM, [
    ('dwChannel', DWORD),
    ('dwPtzChannel', DWORD),
    ('struToPoint', NET_VCA_POINT),
    ('struOriPoint', NET_VCA_POINT),
    ('byRes', BYTE * 56),
])

NET_DVR_DRAG_POS_PARAM = struct_tagNET_DVR_DRAG_POS_PARAM
LPNET_DVR_DRAG_POS_PARAM = POINTER(struct_tagNET_DVR_DRAG_POS_PARAM)
tagNET_DVR_DRAG_POS_PARAM = struct_tagNET_DVR_DRAG_POS_PARAM
