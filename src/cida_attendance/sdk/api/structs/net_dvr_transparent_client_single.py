from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_TRANSPARENT_CLIENT_SINGLE(Structure):
    pass

_S(struct_tagNET_DVR_TRANSPARENT_CLIENT_SINGLE, [
    ('byEnable', BYTE),
    ('byRes1', BYTE * 3),
    ('struIP', NET_DVR_IPADDR),
    ('wPort', WORD),
    ('byRes2', BYTE * 18),
])

NET_DVR_TRANSPARENT_CLIENT_SINGLE = struct_tagNET_DVR_TRANSPARENT_CLIENT_SINGLE
LPNET_DVR_TRANSPARENT_CLIENT_SINGLE = POINTER(struct_tagNET_DVR_TRANSPARENT_CLIENT_SINGLE)
tagNET_DVR_TRANSPARENT_CLIENT_SINGLE = struct_tagNET_DVR_TRANSPARENT_CLIENT_SINGLE
