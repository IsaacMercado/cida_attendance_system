from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DEVICE_NET_USING_INFO(Structure):
    pass

_S(struct_tagNET_DEVICE_NET_USING_INFO, [
    ('dwSize', DWORD),
    ('dwPreview', DWORD),
    ('dwPlayback', DWORD),
    ('dwIPCModule', DWORD),
    ('dwNetDiskRW', DWORD),
    ('res', BYTE * 32),
])

NET_DVR_DEVICE_NET_USING_INFO = struct_tagNET_DEVICE_NET_USING_INFO
LPNET_DVR_DEVICE_NET_USING_INFO = POINTER(struct_tagNET_DEVICE_NET_USING_INFO)
tagNET_DEVICE_NET_USING_INFO = struct_tagNET_DEVICE_NET_USING_INFO
