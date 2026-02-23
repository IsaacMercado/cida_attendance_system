from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .anon_27 import NET_DVR_RGB_COLOR


class struct_tagNET_DVR_OSD_INFO(Structure):
    pass

_S(struct_tagNET_DVR_OSD_INFO, [
    ('byEnabled', BYTE),
    ('byEnabledFlash', BYTE),
    ('byFontSize', BYTE),
    ('byTransparent', BYTE),
    ('struColor', NET_DVR_RGB_COLOR),
    ('wCoordinateX', WORD),
    ('wCoordinateY', WORD),
    ('byContent', BYTE * 256),
    ('byRes', BYTE * 32),
])

NET_DVR_OSD_INFO = struct_tagNET_DVR_OSD_INFO
LPNET_DVR_OSD_INFO = POINTER(struct_tagNET_DVR_OSD_INFO)
tagNET_DVR_OSD_INFO = struct_tagNET_DVR_OSD_INFO
