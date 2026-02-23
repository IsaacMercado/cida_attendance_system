from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_vca_point import NET_VCA_POINT


class struct_tagNET_DVR_THSCREEN(Structure):
    pass

_S(struct_tagNET_DVR_THSCREEN, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byTHOSDDisplay', BYTE),
    ('byRes', BYTE * 2),
    ('struTHOSDPoint', NET_VCA_POINT),
    ('byTimingMode', BYTE),
    ('byRes1', BYTE),
    ('wInterval', WORD),
    ('byRes2', BYTE * 254),
])

NET_DVR_THSCREEN = struct_tagNET_DVR_THSCREEN
LPNET_DVR_THSCREEN = POINTER(struct_tagNET_DVR_THSCREEN)
tagNET_DVR_THSCREEN = struct_tagNET_DVR_THSCREEN
