from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_backup_record_info import NET_DVR_BACKUP_RECORD_INFO


class struct_tagNET_DVR_BACKUP_RECORD_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_BACKUP_RECORD_PARAM, [
    ('dwSize', DWORD),
    ('struChanBackUp', NET_DVR_BACKUP_RECORD_INFO * int((32 + 32))),
    ('struDirectedChanBackUp', NET_DVR_BACKUP_RECORD_INFO),
    ('byRes', BYTE * 256),
])

NET_DVR_BACKUP_RECORD_PARAM = struct_tagNET_DVR_BACKUP_RECORD_PARAM
LPNET_DVR_BACKUP_RECORD_PARAM = POINTER(struct_tagNET_DVR_BACKUP_RECORD_PARAM)
tagNET_DVR_BACKUP_RECORD_PARAM = struct_tagNET_DVR_BACKUP_RECORD_PARAM
