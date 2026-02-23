from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_DEV_STORAGE_CFG(Structure):
    pass

_S(struct_tagNET_DVR_DEV_STORAGE_CFG, [
    ('dwSize', DWORD),
    ('dwCapacityTotal', DWORD),
    ('dwFreeSpaceTotal', DWORD),
    ('dwLockedRecordSpace', DWORD),
    ('dwUnLockedSpace', DWORD),
    ('byRes', BYTE * 512),
])

NET_DVR_DEV_STORAGE_CFG = struct_tagNET_DVR_DEV_STORAGE_CFG
LPNET_DVR_DEV_STORAGE_CFG = POINTER(struct_tagNET_DVR_DEV_STORAGE_CFG)
tagNET_DVR_DEV_STORAGE_CFG = struct_tagNET_DVR_DEV_STORAGE_CFG
