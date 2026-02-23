from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_single_net_disk_info_v40 import NET_DVR_SINGLE_NET_DISK_INFO_V40


class struct_tagNET_DVR_NET_DISKCFG_V40(Structure):
    pass

_S(struct_tagNET_DVR_NET_DISKCFG_V40, [
    ('dwSize', DWORD),
    ('struNetDiskParam', NET_DVR_SINGLE_NET_DISK_INFO_V40 * 16),
])

NET_DVR_NET_DISKCFG_V40 = struct_tagNET_DVR_NET_DISKCFG_V40
LPNET_DVR_NET_DISKCFG_V40 = POINTER(struct_tagNET_DVR_NET_DISKCFG_V40)
tagNET_DVR_NET_DISKCFG_V40 = struct_tagNET_DVR_NET_DISKCFG_V40
