from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_single_netparam import NET_DVR_SINGLE_NETPARAM


class struct_tagNET_DVR_NETPARAM(Structure):
    pass

_S(struct_tagNET_DVR_NETPARAM, [
    ('dwSize', DWORD),
    ('struEtherNet', NET_DVR_SINGLE_NETPARAM * 2),
    ('byRes', BYTE * 64),
])

NET_DVR_NETPARAM = struct_tagNET_DVR_NETPARAM
LPNET_DVR_NETPARAM = POINTER(struct_tagNET_DVR_NETPARAM)
tagNET_DVR_NETPARAM = struct_tagNET_DVR_NETPARAM
