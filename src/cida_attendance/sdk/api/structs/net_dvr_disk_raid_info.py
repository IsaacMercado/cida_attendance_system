from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_DISK_RAID_INFO(Structure):
    pass

_S(struct_tagNET_DVR_DISK_RAID_INFO, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('bySleepStatus', BYTE),
    ('byRes', BYTE * 34),
])

NET_DVR_DISK_RAID_INFO = struct_tagNET_DVR_DISK_RAID_INFO
LPNET_DVR_DISK_RAID_INFO = POINTER(struct_tagNET_DVR_DISK_RAID_INFO)
tagNET_DVR_DISK_RAID_INFO = struct_tagNET_DVR_DISK_RAID_INFO
