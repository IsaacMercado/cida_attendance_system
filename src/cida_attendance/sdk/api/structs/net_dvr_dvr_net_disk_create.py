from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_DVR_NET_DISK_CREATE(Structure):
    pass

_S(struct_tagNET_DVR_DVR_NET_DISK_CREATE, [
    ('dwSize', DWORD),
    ('szRaidName', c_char * 16),
    ('szDvrNetDiskName', c_char * 16),
    ('dwBlockSize', DWORD),
    ('dwHCapacity', DWORD),
    ('dwLCapacity', DWORD),
    ('struWarrantIP', NET_DVR_IPADDR),
    ('byRes', BYTE * 32),
])

NET_DVR_DVR_NET_DISK_CREATE = struct_tagNET_DVR_DVR_NET_DISK_CREATE
LPNET_DVR_DVR_NET_DISK_CREATE = POINTER(struct_tagNET_DVR_DVR_NET_DISK_CREATE)
tagNET_DVR_DVR_NET_DISK_CREATE = struct_tagNET_DVR_DVR_NET_DISK_CREATE
