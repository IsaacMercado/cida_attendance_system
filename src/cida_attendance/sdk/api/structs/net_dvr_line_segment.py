from ctypes import Structure, c_float

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_vca_point import NET_VCA_POINT


class struct_tagNET_DVR_LINE_SEGMENT(Structure):
    pass

_S(struct_tagNET_DVR_LINE_SEGMENT, [
    ('byLineMode', BYTE),
    ('byRes', BYTE * 3),
    ('struStartPoint', NET_VCA_POINT),
    ('struEndPoint', NET_VCA_POINT),
    ('fValue', c_float),
])

NET_DVR_LINE_SEGMENT = struct_tagNET_DVR_LINE_SEGMENT
LPNET_DVR_LINE_SEGMENT = POINTER(struct_tagNET_DVR_LINE_SEGMENT)
tagNET_DVR_LINE_SEGMENT = struct_tagNET_DVR_LINE_SEGMENT
