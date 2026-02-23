from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_DRAWFRAME_DISK_QUOTA_CFG(Structure):
    pass

_S(struct_tagNET_DVR_DRAWFRAME_DISK_QUOTA_CFG, [
    ('dwSize', DWORD),
    ('byPicQuota', BYTE),
    ('byRecordQuota', BYTE),
    ('byDrawFrameRecordQuota', BYTE),
    ('byRes', BYTE * 61),
])

NET_DVR_DRAWFRAME_DISK_QUOTA_CFG = struct_tagNET_DVR_DRAWFRAME_DISK_QUOTA_CFG
LPNET_DVR_DRAWFRAME_DISK_QUOTA_CFG = POINTER(struct_tagNET_DVR_DRAWFRAME_DISK_QUOTA_CFG)
tagNET_DVR_DRAWFRAME_DISK_QUOTA_CFG = struct_tagNET_DVR_DRAWFRAME_DISK_QUOTA_CFG
