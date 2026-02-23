from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ACCESS_DEVICE_CHANNEL_INFO(Structure):
    pass

_S(struct_tagNET_DVR_ACCESS_DEVICE_CHANNEL_INFO, [
    ('dwSize', DWORD),
    ('dwTotalChannelNum', DWORD),
    ('byChannel', BYTE * int((32 + 32))),
    ('byRes', BYTE * 32),
])

NET_DVR_ACCESS_DEVICE_CHANNEL_INFO = struct_tagNET_DVR_ACCESS_DEVICE_CHANNEL_INFO
LPNET_DVR_ACCESS_DEVICE_CHANNEL_INFO = POINTER(struct_tagNET_DVR_ACCESS_DEVICE_CHANNEL_INFO)
tagNET_DVR_ACCESS_DEVICE_CHANNEL_INFO = struct_tagNET_DVR_ACCESS_DEVICE_CHANNEL_INFO
