from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_SINGLE_NETPARAM(Structure):
    pass

_S(struct_tagNET_DVR_SINGLE_NETPARAM, [
    ('dwSize', DWORD),
    ('byUseDhcp', BYTE),
    ('byRes1', BYTE * 3),
    ('struDevIP', NET_DVR_IPADDR),
    ('struSubnetMask', NET_DVR_IPADDR),
    ('struGateway', NET_DVR_IPADDR),
    ('wDevPort', WORD),
    ('byMACAddr', BYTE * 6),
    ('byRes2', BYTE * 16),
])

NET_DVR_SINGLE_NETPARAM = struct_tagNET_DVR_SINGLE_NETPARAM
LPNET_DVR_SINGLE_NETPARAM = POINTER(struct_tagNET_DVR_SINGLE_NETPARAM)
tagNET_DVR_SINGLE_NETPARAM = struct_tagNET_DVR_SINGLE_NETPARAM
