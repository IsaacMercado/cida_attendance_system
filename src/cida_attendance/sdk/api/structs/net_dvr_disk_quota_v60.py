from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_DISK_QUOTA_V60(Structure):
    pass

_S(struct_tagNET_DVR_DISK_QUOTA_V60, [
    ('byQuotaType', BYTE),
    ('byRes1', BYTE * 5),
    ('wStoragePeriod', WORD),
    ('dwHCapacity', DWORD),
    ('dwLCapacity', DWORD),
    ('dwHUsedSpace', DWORD),
    ('dwLUsedSpace', DWORD),
    ('byQuotaRatio', BYTE),
    ('byRes2', BYTE * 23),
])

NET_DVR_DISK_QUOTA_V60 = struct_tagNET_DVR_DISK_QUOTA_V60
LPNET_DVR_DISK_QUOTA_V60 = POINTER(struct_tagNET_DVR_DISK_QUOTA_V60)
tagNET_DVR_DISK_QUOTA_V60 = struct_tagNET_DVR_DISK_QUOTA_V60
