from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PARKSPACE_INFO(Structure):
    pass

_S(struct_tagNET_DVR_PARKSPACE_INFO, [
    ('byParkSpaceAttribute', BYTE),
    ('byRes', BYTE * 23),
])

NET_DVR_PARKSPACE_INFO = struct_tagNET_DVR_PARKSPACE_INFO
LPNET_DVR_PARKSPACE_INFO = POINTER(struct_tagNET_DVR_PARKSPACE_INFO)
tagNET_DVR_PARKSPACE_INFO = struct_tagNET_DVR_PARKSPACE_INFO
