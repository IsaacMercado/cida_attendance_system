from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_VCA_DEV_INFO(Structure):
    pass

_S(struct_tagNET_VCA_DEV_INFO, [
    ('struDevIP', NET_DVR_IPADDR),
    ('wPort', WORD),
    ('byChannel', BYTE),
    ('byIvmsChannel', BYTE),
])

NET_VCA_DEV_INFO = struct_tagNET_VCA_DEV_INFO
LPNET_VCA_DEV_INFO = POINTER(struct_tagNET_VCA_DEV_INFO)
tagNET_VCA_DEV_INFO = struct_tagNET_VCA_DEV_INFO
