from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_6 import NET_DVR_SCHEDTIME


class struct_tagNET_DVR_HOLIDAY_HANDLE(Structure):
    pass

_S(struct_tagNET_DVR_HOLIDAY_HANDLE, [
    ('dwSize', DWORD),
    ('struAlarmTime', NET_DVR_SCHEDTIME * 8),
    ('byRes2', BYTE * 240),
])

NET_DVR_HOLIDAY_HANDLE = struct_tagNET_DVR_HOLIDAY_HANDLE
LPNET_DVR_HOLIDAY_HANDLE = POINTER(struct_tagNET_DVR_HOLIDAY_HANDLE)
tagNET_DVR_HOLIDAY_HANDLE = struct_tagNET_DVR_HOLIDAY_HANDLE
