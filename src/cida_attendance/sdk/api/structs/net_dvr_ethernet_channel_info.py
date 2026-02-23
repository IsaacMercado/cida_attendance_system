from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ETHERNET_CHANNEL_INFO(Structure):
    pass

_S(struct_tagNET_DVR_ETHERNET_CHANNEL_INFO, [
    ('dwSize', DWORD),
    ('byConverge', BYTE * 8),
    ('byRes', BYTE * 32),
])

NET_DVR_ETHERNET_CHANNEL_INFO = struct_tagNET_DVR_ETHERNET_CHANNEL_INFO
LPNET_DVR_ETHERNET_CHANNEL_INFO = POINTER(struct_tagNET_DVR_ETHERNET_CHANNEL_INFO)
tagNET_DVR_ETHERNET_CHANNEL_INFO = struct_tagNET_DVR_ETHERNET_CHANNEL_INFO
