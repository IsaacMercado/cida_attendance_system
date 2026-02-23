from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_time_ex import NET_DVR_TIME_EX


class struct_tagNET_DVR_DEVICE_FILE_INFO(Structure):
    pass

_S(struct_tagNET_DVR_DEVICE_FILE_INFO, [
    ('dwSize', DWORD),
    ('sFileName', BYTE * 32),
    ('dwManageNo', DWORD),
    ('struTime', NET_DVR_TIME_EX),
    ('byUsed', BYTE),
    ('byRes', BYTE * 127),
])

NET_DVR_DEVICE_FILE_INFO = struct_tagNET_DVR_DEVICE_FILE_INFO
LPNET_DVR_DEVICE_FILE_INFO = POINTER(struct_tagNET_DVR_DEVICE_FILE_INFO)
tagNET_DVR_DEVICE_FILE_INFO = struct_tagNET_DVR_DEVICE_FILE_INFO
