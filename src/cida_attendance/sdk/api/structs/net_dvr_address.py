from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_ADDRESS(Structure):
    pass

_S(struct_tagNET_DVR_ADDRESS, [
    ('struIP', NET_DVR_IPADDR),
    ('wPort', WORD),
    ('byRes', BYTE * 2),
])

NET_DVR_ADDRESS = struct_tagNET_DVR_ADDRESS
LPNET_DVR_ADDRESS = POINTER(struct_tagNET_DVR_ADDRESS)
tagNET_DVR_ADDRESS = struct_tagNET_DVR_ADDRESS
