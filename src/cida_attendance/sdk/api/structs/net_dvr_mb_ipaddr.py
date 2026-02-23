from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_MB_IPADDR(Structure):
    pass

_S(struct_tagNET_DVR_MB_IPADDR, [
    ('struIP', NET_DVR_IPADDR),
    ('wPort', WORD),
    ('byRes', BYTE * 2),
])

NET_DVR_MB_IPADDR = struct_tagNET_DVR_MB_IPADDR
LPNET_DVR_MB_IPADDR = POINTER(struct_tagNET_DVR_MB_IPADDR)
tagNET_DVR_MB_IPADDR = struct_tagNET_DVR_MB_IPADDR
