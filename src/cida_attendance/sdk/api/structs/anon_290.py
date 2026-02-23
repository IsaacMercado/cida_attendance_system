from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME
from .anon_2 import NET_DVR_IPADDR


class struct_anon_290(Structure):
    pass

_S(struct_anon_290, [
    ('strLogTime', NET_DVR_TIME),
    ('dwMajorType', DWORD),
    ('dwMinorType', DWORD),
    ('sPanelUser', BYTE * 16),
    ('sNetUser', BYTE * 16),
    ('struRemoteHostAddr', NET_DVR_IPADDR),
    ('dwParaType', DWORD),
    ('dwChannel', DWORD),
    ('dwDiskNumber', DWORD),
    ('dwAlarmInPort', DWORD),
    ('dwAlarmOutPort', DWORD),
    ('dwInfoLen', DWORD),
    ('byDevSequence', BYTE),
    ('byMacAddr', BYTE * 6),
    ('sSerialNumber', BYTE * 48),
    ('sInfo', c_char * int((((11840 - 48) - 6) - 1))),
])

NET_DVR_LOG_MATRIX = struct_anon_290
LPNET_DVR_LOG_MATRIX = POINTER(struct_anon_290)
