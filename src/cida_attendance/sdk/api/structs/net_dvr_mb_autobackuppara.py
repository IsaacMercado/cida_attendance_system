from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_6 import NET_DVR_SCHEDTIME


class struct_tagNET_DVR_MB_AUTOBACKUPPARA(Structure):
    pass

_S(struct_tagNET_DVR_MB_AUTOBACKUPPARA, [
    ('dwSize', DWORD),
    ('byEnableAutoBackup', BYTE),
    ('byRes1', BYTE * 3),
    ('byBackupChannel', BYTE * int((32 + 32))),
    ('byBackupDays', BYTE * int((32 + 32))),
    ('byBackupFileType', BYTE * int((32 + 32))),
    ('struBackupTime', (NET_DVR_SCHEDTIME * 2) * int((32 + 32))),
    ('byRes2', BYTE * 36),
])

NET_DVR_MB_AUTOBACKUPPARA = struct_tagNET_DVR_MB_AUTOBACKUPPARA
LPNET_DVR_MB_AUTOBACKUPPARA = POINTER(struct_tagNET_DVR_MB_AUTOBACKUPPARA)
tagNET_DVR_MB_AUTOBACKUPPARA = struct_tagNET_DVR_MB_AUTOBACKUPPARA
