from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_DISK_QUOTA(Structure):
    pass

_S(struct_tagNET_DVR_DISK_QUOTA, [
    ('byQuotaType', BYTE),
    ('byRes1', BYTE * 5),
    ('wStoragePeriod', WORD),
    ('dwHCapacity', DWORD),
    ('dwLCapacity', DWORD),
    ('dwHUsedSpace', DWORD),
    ('dwLUsedSpace', DWORD),
    ('byQuotaRatio', BYTE),
    ('byRes2', BYTE * 21),
])

NET_DVR_DISK_QUOTA = struct_tagNET_DVR_DISK_QUOTA
LPNET_DVR_DISK_QUOTA = POINTER(struct_tagNET_DVR_DISK_QUOTA)
tagNET_DVR_DISK_QUOTA = struct_tagNET_DVR_DISK_QUOTA
