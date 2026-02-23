from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_server_device_cfg import NET_DVR_SERVER_DEVICE_CFG


class struct_tagNET_DVR_SERVER_DEVICE_INFO(Structure):
    pass

_S(struct_tagNET_DVR_SERVER_DEVICE_INFO, [
    ('dwSize', DWORD),
    ('dwDeviceNum', DWORD),
    ('struDeviceCfg', NET_DVR_SERVER_DEVICE_CFG * 16),
    ('byRes', BYTE * 200),
])

NET_DVR_SERVER_DEVICE_INFO = struct_tagNET_DVR_SERVER_DEVICE_INFO
LPNET_DVR_SERVER_DEVICE_INFO = POINTER(struct_tagNET_DVR_SERVER_DEVICE_INFO)
tagNET_DVR_SERVER_DEVICE_INFO = struct_tagNET_DVR_SERVER_DEVICE_INFO
