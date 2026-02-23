from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_phy_disk_info import NET_DVR_PHY_DISK_INFO


class struct_tagNET_DVR_PHY_DISK_LIST(Structure):
    pass

_S(struct_tagNET_DVR_PHY_DISK_LIST, [
    ('dwSize', DWORD),
    ('dwCount', DWORD),
    ('struPhyDiskInfo', NET_DVR_PHY_DISK_INFO * 16),
])

NET_DVR_PHY_DISK_LIST = struct_tagNET_DVR_PHY_DISK_LIST
LPNET_DVR_PHY_DISK_LIST = POINTER(struct_tagNET_DVR_PHY_DISK_LIST)
tagNET_DVR_PHY_DISK_LIST = struct_tagNET_DVR_PHY_DISK_LIST
