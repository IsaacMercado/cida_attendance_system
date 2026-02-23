from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_disk_quota import NET_DVR_DISK_QUOTA


class struct_tagNET_DVR_DISK_QUOTA_CFG(Structure):
    pass

_S(struct_tagNET_DVR_DISK_QUOTA_CFG, [
    ('dwSize', DWORD),
    ('struPicQuota', NET_DVR_DISK_QUOTA),
    ('struRecordQuota', NET_DVR_DISK_QUOTA),
    ('struAddInfoQuota', NET_DVR_DISK_QUOTA),
    ('byRes', BYTE * 12),
])

NET_DVR_DISK_QUOTA_CFG = struct_tagNET_DVR_DISK_QUOTA_CFG
LPNET_DVR_DISK_QUOTA_CFG = POINTER(struct_tagNET_DVR_DISK_QUOTA_CFG)
tagNET_DVR_DISK_QUOTA_CFG = struct_tagNET_DVR_DISK_QUOTA_CFG
