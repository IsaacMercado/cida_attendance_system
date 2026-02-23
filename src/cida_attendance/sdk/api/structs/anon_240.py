from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from .net_dvr_stream_info import NET_DVR_STREAM_INFO


class struct_anon_240(Structure):
    pass

_S(struct_anon_240, [
    ('struIDInfo', NET_DVR_STREAM_INFO),
    ('dwCmdType', DWORD),
    ('byBackupVolumeNum', BYTE),
    ('byRes', BYTE * 223),
])

