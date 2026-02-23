from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_time_v30 import NET_DVR_TIME_V30


class struct_tagNET_ITS_SINGLE_DEVICE_INFO(Structure):
    pass

_S(struct_tagNET_ITS_SINGLE_DEVICE_INFO, [
    ('dwDeviceType', DWORD),
    ('dwDirID', DWORD),
    ('dwLaneID', DWORD),
    ('dwDeviceState', DWORD),
    ('byDeviceName', BYTE * 32),
    ('byDeviceID', BYTE * 48),
    ('struTriggerTime', NET_DVR_TIME_V30),
    ('byRelateChan', BYTE),
    ('byRes', BYTE * 3),
])

NET_ITS_SINGLE_DEVICE_INFO = struct_tagNET_ITS_SINGLE_DEVICE_INFO
LPNET_ITS_SINGLE_DEVICE_INFO = POINTER(struct_tagNET_ITS_SINGLE_DEVICE_INFO)
tagNET_ITS_SINGLE_DEVICE_INFO = struct_tagNET_ITS_SINGLE_DEVICE_INFO
