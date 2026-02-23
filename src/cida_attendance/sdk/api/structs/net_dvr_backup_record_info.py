from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_BACKUP_RECORD_INFO(Structure):
    pass

_S(struct_tagNET_DVR_BACKUP_RECORD_INFO, [
    ('byEnable', BYTE),
    ('byRes', BYTE * 11),
    ('dwStreamType', DWORD),
])

NET_DVR_BACKUP_RECORD_INFO = struct_tagNET_DVR_BACKUP_RECORD_INFO
LPNET_DVR_BACKUP_RECORD_INFO = POINTER(struct_tagNET_DVR_BACKUP_RECORD_INFO)
tagNET_DVR_BACKUP_RECORD_INFO = struct_tagNET_DVR_BACKUP_RECORD_INFO
