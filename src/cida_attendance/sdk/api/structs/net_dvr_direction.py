from ctypes import Structure

from ..base_classes import _S
from ..ctypes_preamble import POINTER
from .net_vca_point import NET_VCA_POINT


class struct_tagNET_DVR_DIRECTION(Structure):
    pass

_S(struct_tagNET_DVR_DIRECTION, [
    ('struStartPoint', NET_VCA_POINT),
    ('struEndPoint', NET_VCA_POINT),
])

NET_DVR_DIRECTION = struct_tagNET_DVR_DIRECTION
LPNET_DVR_DIRECTION = POINTER(struct_tagNET_DVR_DIRECTION)
tagNET_DVR_DIRECTION = struct_tagNET_DVR_DIRECTION
