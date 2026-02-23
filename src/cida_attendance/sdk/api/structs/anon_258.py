from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from .net_dvr_stream_info import NET_DVR_STREAM_INFO


class struct_anon_258(Structure):
    pass

_S(struct_anon_258, [
    ('struIDInfo', NET_DVR_STREAM_INFO),
    ('dwCmdType', DWORD),
    ('byBackupVolumeNum', BYTE),
    ('byRes1', BYTE * 3),
    ('byArchiveLabel', BYTE * 64),
    ('byRes', BYTE * 656),
])

