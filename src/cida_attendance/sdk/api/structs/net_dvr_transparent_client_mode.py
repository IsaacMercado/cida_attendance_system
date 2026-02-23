from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_transparent_client_single import NET_DVR_TRANSPARENT_CLIENT_SINGLE


class struct_tagNET_DVR_TRANSPARENT_CLIENT_MODE(Structure):
    pass

_S(struct_tagNET_DVR_TRANSPARENT_CLIENT_MODE, [
    ('struClientSingle', NET_DVR_TRANSPARENT_CLIENT_SINGLE * 4),
    ('byRes', BYTE * 320),
])

NET_DVR_TRANSPARENT_CLIENT_MODE = struct_tagNET_DVR_TRANSPARENT_CLIENT_MODE
LPNET_DVR_TRANSPARENT_CLIENT_MODE = POINTER(struct_tagNET_DVR_TRANSPARENT_CLIENT_MODE)
tagNET_DVR_TRANSPARENT_CLIENT_MODE = struct_tagNET_DVR_TRANSPARENT_CLIENT_MODE
