from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_anon_10(Structure):
    pass

_S(struct_anon_10, [
    ('struDVRIP', NET_DVR_IPADDR),
    ('struDVRIPMask', NET_DVR_IPADDR),
    ('dwNetInterface', DWORD),
    ('wDVRPort', WORD),
    ('wMTU', WORD),
    ('byMACAddr', BYTE * 6),
    ('byEthernetPortNo', BYTE),
    ('byRes', BYTE * 1),
])

NET_DVR_ETHERNET_V30 = struct_anon_10
LPNET_DVR_ETHERNET_V30 = POINTER(struct_anon_10)
