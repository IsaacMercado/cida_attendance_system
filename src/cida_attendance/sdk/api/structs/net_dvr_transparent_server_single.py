from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_TRANSPARENT_SERVER_SINGLE(Structure):
    pass

_S(struct_tagNET_DVR_TRANSPARENT_SERVER_SINGLE, [
    ('byEnable', BYTE),
    ('byRes1', BYTE * 3),
    ('struIP', NET_DVR_IPADDR),
    ('byRes2', BYTE * 16),
])

NET_DVR_TRANSPARENT_SERVER_SINGLE = struct_tagNET_DVR_TRANSPARENT_SERVER_SINGLE
LPNET_DVR_TRANSPARENT_SERVER_SINGLE = POINTER(struct_tagNET_DVR_TRANSPARENT_SERVER_SINGLE)
tagNET_DVR_TRANSPARENT_SERVER_SINGLE = struct_tagNET_DVR_TRANSPARENT_SERVER_SINGLE
