from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_object_color_union import NET_DVR_OBJECT_COLOR_UNION


class struct_tagNET_DVR_OBJECT_COLOR(Structure):
    pass

_S(struct_tagNET_DVR_OBJECT_COLOR, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byColorMode', BYTE),
    ('byRes1', BYTE * 2),
    ('uObjColor', NET_DVR_OBJECT_COLOR_UNION),
    ('byRes2', BYTE * 64),
])

NET_DVR_OBJECT_COLOR = struct_tagNET_DVR_OBJECT_COLOR
LPNET_DVR_OBJECT_COLOR = POINTER(struct_tagNET_DVR_OBJECT_COLOR)
tagNET_DVR_OBJECT_COLOR = struct_tagNET_DVR_OBJECT_COLOR
