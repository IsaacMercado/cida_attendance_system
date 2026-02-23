from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_ITS_ILLEGAL_INFO(Structure):
    pass

_S(struct_tagNET_ITS_ILLEGAL_INFO, [
    ('byIllegalInfo', BYTE * 64),
    ('byRes', BYTE * 256),
])

NET_ITS_ILLEGAL_INFO = struct_tagNET_ITS_ILLEGAL_INFO
LPNET_ITS_ILLEGAL_INFO = POINTER(struct_tagNET_ITS_ILLEGAL_INFO)
tagNET_ITS_ILLEGAL_INFO = struct_tagNET_ITS_ILLEGAL_INFO
