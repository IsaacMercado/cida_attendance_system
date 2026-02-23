from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_202 import NET_DVR_FINDDATA_V30


class struct_tagNET_DVR_BACKUP_NAME_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_BACKUP_NAME_PARAM, [
    ('dwFileNum', DWORD),
    ('struFileList', NET_DVR_FINDDATA_V30 * 20),
    ('byDiskDes', BYTE * 32),
    ('byWithPlayer', BYTE),
    ('byContinue', BYTE),
    ('byRes', BYTE * 34),
])

NET_DVR_BACKUP_NAME_PARAM = struct_tagNET_DVR_BACKUP_NAME_PARAM
LPNET_DVR_BACKUP_NAME_PARAM = POINTER(struct_tagNET_DVR_BACKUP_NAME_PARAM)
tagNET_DVR_BACKUP_NAME_PARAM = struct_tagNET_DVR_BACKUP_NAME_PARAM
