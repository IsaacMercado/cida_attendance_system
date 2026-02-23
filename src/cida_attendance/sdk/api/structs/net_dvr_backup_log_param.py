from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_BACKUP_LOG_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_BACKUP_LOG_PARAM, [
    ('dwSize', DWORD),
    ('byDiskDesc', BYTE * 32),
    ('byHardDisk', BYTE * 128),
    ('byBackupHardDiskNum', BYTE),
    ('byContinue', BYTE),
    ('byAllLogBackUp', BYTE),
    ('byRes', BYTE * 29),
])

NET_DVR_BACKUP_LOG_PARAM = struct_tagNET_DVR_BACKUP_LOG_PARAM
LPNET_DVR_BACKUP_LOG_PARAM = POINTER(struct_tagNET_DVR_BACKUP_LOG_PARAM)
tagNET_DVR_BACKUP_LOG_PARAM = struct_tagNET_DVR_BACKUP_LOG_PARAM
