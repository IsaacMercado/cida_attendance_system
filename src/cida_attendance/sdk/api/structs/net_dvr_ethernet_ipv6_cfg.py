from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ETHERNET_IPV6_CFG(Structure):
    pass

_S(struct_tagNET_DVR_ETHERNET_IPV6_CFG, [
    ('dwSize', DWORD),
    ('byState', BYTE),
    ('byRes1', BYTE * 3),
    ('byIPv6', BYTE * 64),
    ('byRes', BYTE * 64),
])

NET_DVR_ETHERNET_IPV6_CFG = struct_tagNET_DVR_ETHERNET_IPV6_CFG
LPNET_DVR_ETHERNET_IPV6_CFG = POINTER(struct_tagNET_DVR_ETHERNET_IPV6_CFG)
tagNET_DVR_ETHERNET_IPV6_CFG = struct_tagNET_DVR_ETHERNET_IPV6_CFG
