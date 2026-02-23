from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_device_type import NET_DVR_DEVICE_TYPE


class struct_tagNET_DVR_DEVICE_TYPE_LIST(Structure):
    pass

_S(struct_tagNET_DVR_DEVICE_TYPE_LIST, [
    ('dwSize', DWORD),
    ('dwTypeNum', DWORD),
    ('struDeviceType', NET_DVR_DEVICE_TYPE * 256),
    ('byRes', BYTE * 12),
])

NET_DVR_DEVICE_TYPE_LIST = struct_tagNET_DVR_DEVICE_TYPE_LIST
LPNET_DVR_DEVICE_TYPE_LIST = POINTER(struct_tagNET_DVR_DEVICE_TYPE_LIST)
tagNET_DVR_DEVICE_TYPE_LIST = struct_tagNET_DVR_DEVICE_TYPE_LIST
