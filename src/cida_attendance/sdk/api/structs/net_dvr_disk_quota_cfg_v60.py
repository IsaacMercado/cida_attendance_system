from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_disk_quota_v60 import NET_DVR_DISK_QUOTA_V60


class struct_tagNET_DVR_DISK_QUOTA_CFG_V60(Structure):
    pass

_S(struct_tagNET_DVR_DISK_QUOTA_CFG_V60, [
    ('dwSize', DWORD),
    ('struPicQuota', NET_DVR_DISK_QUOTA_V60),
    ('struRecordQuota', NET_DVR_DISK_QUOTA_V60),
    ('struAddInfoQuota', NET_DVR_DISK_QUOTA_V60),
    ('struPubInfoFile', NET_DVR_DISK_QUOTA_V60),
    ('byRes', BYTE * 256),
])

NET_DVR_DISK_QUOTA_CFG_V60 = struct_tagNET_DVR_DISK_QUOTA_CFG_V60
LPNET_DVR_DISK_QUOTA_CFG_V60 = POINTER(struct_tagNET_DVR_DISK_QUOTA_CFG_V60)
tagNET_DVR_DISK_QUOTA_CFG_V60 = struct_tagNET_DVR_DISK_QUOTA_CFG_V60
