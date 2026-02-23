from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, LONG
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME


class struct_tagNET_DVR_BACKUP_TIME_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_BACKUP_TIME_PARAM, [
    ('lChannel', LONG),
    ('struStartTime', NET_DVR_TIME),
    ('struStopTime', NET_DVR_TIME),
    ('byDiskDes', BYTE * 32),
    ('byWithPlayer', BYTE),
    ('byContinue', BYTE),
    ('byDrawFrame', BYTE),
    ('byUseBackCfgParam', BYTE),
    ('dwStreamType', DWORD),
    ('byRes', BYTE * 28),
])

NET_DVR_BACKUP_TIME_PARAM = struct_tagNET_DVR_BACKUP_TIME_PARAM
LPNET_DVR_BACKUP_TIME_PARAM = POINTER(struct_tagNET_DVR_BACKUP_TIME_PARAM)
tagNET_DVR_BACKUP_TIME_PARAM = struct_tagNET_DVR_BACKUP_TIME_PARAM
