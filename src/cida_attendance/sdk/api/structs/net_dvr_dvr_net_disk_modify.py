from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_DVR_NET_DISK_MODIFY(Structure):
    pass

_S(struct_tagNET_DVR_DVR_NET_DISK_MODIFY, [
    ('dwSize', DWORD),
    ('szOldDvrNetDiskName', c_char * 16),
    ('szNewDvrNetDiskName', c_char * 16),
    ('struWarrantIP', NET_DVR_IPADDR),
    ('byRes', BYTE * 32),
])

NET_DVR_DVR_NET_DISK_MODIFY = struct_tagNET_DVR_DVR_NET_DISK_MODIFY
LPNET_DVR_DVR_NET_DISK_MODIFY = POINTER(struct_tagNET_DVR_DVR_NET_DISK_MODIFY)
tagNET_DVR_DVR_NET_DISK_MODIFY = struct_tagNET_DVR_DVR_NET_DISK_MODIFY
