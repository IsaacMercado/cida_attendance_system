from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_DIGITALSCREEN(Structure):
    pass

_S(struct_tagNET_DVR_DIGITALSCREEN, [
    ('struAddress', NET_DVR_IPADDR),
    ('wPort', WORD),
    ('byRes', BYTE * 26),
])

NET_DVR_DIGITALSCREEN = struct_tagNET_DVR_DIGITALSCREEN
LPNET_DVR_DIGITALSCREEN = POINTER(struct_tagNET_DVR_DIGITALSCREEN)
tagNET_DVR_DIGITALSCREEN = struct_tagNET_DVR_DIGITALSCREEN
