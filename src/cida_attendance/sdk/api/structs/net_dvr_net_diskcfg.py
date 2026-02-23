from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_single_net_disk_info import NET_DVR_SINGLE_NET_DISK_INFO


class struct_tagNET_DVR_NET_DISKCFG(Structure):
    pass

_S(struct_tagNET_DVR_NET_DISKCFG, [
    ('dwSize', DWORD),
    ('struNetDiskParam', NET_DVR_SINGLE_NET_DISK_INFO * 16),
])

NET_DVR_NET_DISKCFG = struct_tagNET_DVR_NET_DISKCFG
LPNET_DVR_NET_DISKCFG = POINTER(struct_tagNET_DVR_NET_DISKCFG)
tagNET_DVR_NET_DISKCFG = struct_tagNET_DVR_NET_DISKCFG
