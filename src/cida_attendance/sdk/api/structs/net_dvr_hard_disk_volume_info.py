from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_hard_disk_single_volume_info import NET_DVR_HARD_DISK_SINGLE_VOLUME_INFO


class struct_tagNET_DVR_HARD_DISK_VOLUME_INFO(Structure):
    pass

_S(struct_tagNET_DVR_HARD_DISK_VOLUME_INFO, [
    ('dwSize', DWORD),
    ('dwHDVolumeCount', DWORD),
    ('struSingleVolumeInfo', NET_DVR_HARD_DISK_SINGLE_VOLUME_INFO * 33),
    ('byRes', BYTE * 128),
])

NET_DVR_HARD_DISK_VOLUME_INFO = struct_tagNET_DVR_HARD_DISK_VOLUME_INFO
LPNET_DVR_HARD_DISK_VOLUME_INFO = POINTER(struct_tagNET_DVR_HARD_DISK_VOLUME_INFO)
tagNET_DVR_HARD_DISK_VOLUME_INFO = struct_tagNET_DVR_HARD_DISK_VOLUME_INFO
