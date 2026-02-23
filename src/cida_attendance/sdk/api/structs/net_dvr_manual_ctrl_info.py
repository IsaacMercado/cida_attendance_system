from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_vca_point import NET_VCA_POINT


class struct_tagNET_DVR_MANUAL_CTRL_INFO(Structure):
    pass

_S(struct_tagNET_DVR_MANUAL_CTRL_INFO, [
    ('struCtrlPoint', NET_VCA_POINT),
    ('byRes', BYTE * 8),
])

NET_DVR_MANUAL_CTRL_INFO = struct_tagNET_DVR_MANUAL_CTRL_INFO
LPNET_DVR_MANUAL_CTRL_INFO = POINTER(struct_tagNET_DVR_MANUAL_CTRL_INFO)
tagNET_DVR_MANUAL_CTRL_INFO = struct_tagNET_DVR_MANUAL_CTRL_INFO
