from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME


class struct_anon_4(Structure):
    pass

_S(struct_anon_4, [
    ('strLogTime', NET_DVR_TIME),
    ('dwMajorType', DWORD),
    ('dwMinorType', DWORD),
    ('sPanelUser', BYTE * 16),
    ('sNetUser', BYTE * 16),
    ('sRemoteHostAddr', c_char * 16),
    ('dwParaType', DWORD),
    ('dwChannel', DWORD),
    ('dwDiskNumber', DWORD),
    ('dwAlarmInPort', DWORD),
    ('dwAlarmOutPort', DWORD),
])

NET_DVR_LOG = struct_anon_4
LPNET_DVR_LOG = POINTER(struct_anon_4)
