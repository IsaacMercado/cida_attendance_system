from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_HARD_DISK_SINGLE_VOLUME_INFO(Structure):
    pass

_S(struct_tagNET_DVR_HARD_DISK_SINGLE_VOLUME_INFO, [
    ('dwSize', DWORD),
    ('byHDVolumeNo', BYTE),
    ('byType', BYTE),
    ('byRes1', BYTE * 2),
    ('dwCapacity', DWORD),
    ('dwFreeSpace', DWORD),
    ('byHDVolumeName', BYTE * 36),
    ('byLoopCover', BYTE),
    ('byRes', BYTE * 63),
])

NET_DVR_HARD_DISK_SINGLE_VOLUME_INFO = struct_tagNET_DVR_HARD_DISK_SINGLE_VOLUME_INFO
LPNET_DVR_HARD_DISK_SINGLE_VOLUME_INFO = POINTER(struct_tagNET_DVR_HARD_DISK_SINGLE_VOLUME_INFO)
tagNET_DVR_HARD_DISK_SINGLE_VOLUME_INFO = struct_tagNET_DVR_HARD_DISK_SINGLE_VOLUME_INFO
