from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_313 import NET_DVR_FIND_PICTURE


class struct_tagNET_DVR_BACKUP_PICTURE_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_BACKUP_PICTURE_PARAM, [
    ('dwSize', DWORD),
    ('dwPicNum', DWORD),
    ('struPicture', NET_DVR_FIND_PICTURE * 50),
    ('byDiskDes', BYTE * 32),
    ('byWithPlayer', BYTE),
    ('byContinue', BYTE),
    ('byRes', BYTE * 34),
])

NET_DVR_BACKUP_PICTURE_PARAM = struct_tagNET_DVR_BACKUP_PICTURE_PARAM
LPNET_DVR_BACKUP_PICTURE_PARAM = POINTER(struct_tagNET_DVR_BACKUP_PICTURE_PARAM)
tagNET_DVR_BACKUP_PICTURE_PARAM = struct_tagNET_DVR_BACKUP_PICTURE_PARAM
