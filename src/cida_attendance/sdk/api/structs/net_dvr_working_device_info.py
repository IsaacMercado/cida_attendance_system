from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR
from .net_dvr_time_ex import NET_DVR_TIME_EX


class struct_tagNET_DVR_WORKING_DEVICE_INFO(Structure):
    pass

_S(struct_tagNET_DVR_WORKING_DEVICE_INFO, [
    ('struIP', NET_DVR_IPADDR),
    ('byLinkStatus', BYTE),
    ('byWorkStatus', BYTE),
    ('byBacupStatus', BYTE),
    ('bySyncProgress', BYTE),
    ('struSyncBeginTime', NET_DVR_TIME_EX),
    ('struSyncEndTime', NET_DVR_TIME_EX),
    ('szSerialNumber', c_char * 48),
    ('dwSoftwareVersion', DWORD),
    ('byWorkingDeviceGUID', BYTE * 16),
    ('szDevTypeName', c_char * 24),
    ('wDevType', WORD),
])

NET_DVR_WORKING_DEVICE_INFO = struct_tagNET_DVR_WORKING_DEVICE_INFO
LPNET_DVR_WORKING_DEVICE_INFO = POINTER(struct_tagNET_DVR_WORKING_DEVICE_INFO)
tagNET_DVR_WORKING_DEVICE_INFO = struct_tagNET_DVR_WORKING_DEVICE_INFO
