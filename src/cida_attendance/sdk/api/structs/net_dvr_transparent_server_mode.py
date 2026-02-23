from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_transparent_server_single import NET_DVR_TRANSPARENT_SERVER_SINGLE


class struct_tagNET_DVR_TRANSPARENT_SERVER_MODE(Structure):
    pass

_S(struct_tagNET_DVR_TRANSPARENT_SERVER_MODE, [
    ('wPort', WORD),
    ('byRes1', BYTE * 2),
    ('struServerSingle', NET_DVR_TRANSPARENT_SERVER_SINGLE * 4),
    ('byRes2', BYTE * 332),
])

NET_DVR_TRANSPARENT_SERVER_MODE = struct_tagNET_DVR_TRANSPARENT_SERVER_MODE
LPNET_DVR_TRANSPARENT_SERVER_MODE = POINTER(struct_tagNET_DVR_TRANSPARENT_SERVER_MODE)
tagNET_DVR_TRANSPARENT_SERVER_MODE = struct_tagNET_DVR_TRANSPARENT_SERVER_MODE
