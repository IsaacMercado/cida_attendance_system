from ctypes import Structure, c_char

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_working_device_info import NET_DVR_WORKING_DEVICE_INFO


class struct_tagNET_DVR_WORKING_DEVICE_INFO_V50(Structure):
    pass

_S(struct_tagNET_DVR_WORKING_DEVICE_INFO_V50, [
    ('struWorkingDeviceInfo', NET_DVR_WORKING_DEVICE_INFO),
    ('szUserName', c_char * 32),
    ('byRes', BYTE * 32),
])

NET_DVR_WORKING_DEVICE_INFO_V50 = struct_tagNET_DVR_WORKING_DEVICE_INFO_V50
LPNET_DVR_WORKING_DEVICE_INFO_V50 = POINTER(struct_tagNET_DVR_WORKING_DEVICE_INFO_V50)
tagNET_DVR_WORKING_DEVICE_INFO_V50 = struct_tagNET_DVR_WORKING_DEVICE_INFO_V50
