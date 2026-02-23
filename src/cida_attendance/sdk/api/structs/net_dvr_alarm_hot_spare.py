from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_ALARM_HOT_SPARE(Structure):
    pass

_S(struct_tagNET_DVR_ALARM_HOT_SPARE, [
    ('dwSize', DWORD),
    ('dwExceptionCase', DWORD),
    ('struDeviceIP', NET_DVR_IPADDR),
    ('byRes', BYTE * 256),
])

NET_DVR_ALARM_HOT_SPARE = struct_tagNET_DVR_ALARM_HOT_SPARE
LPNET_DVR_ALARM_HOT_SPARE = POINTER(struct_tagNET_DVR_ALARM_HOT_SPARE)
tagNET_DVR_ALARM_HOT_SPARE = struct_tagNET_DVR_ALARM_HOT_SPARE
