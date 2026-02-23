from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_DVR_NET_DISK_DEL_(Structure):
    pass

_S(struct_tagNET_DVR_DVR_NET_DISK_DEL_, [
    ('dwSize', DWORD),
    ('szDvrNetDiskName', c_char * 16),
    ('byRes', BYTE * 32),
])

NET_DVR_DVR_NET_DISK_DEL = struct_tagNET_DVR_DVR_NET_DISK_DEL_
LPNET_DVR_DVR_NET_DISK_DEL = POINTER(struct_tagNET_DVR_DVR_NET_DISK_DEL_)
tagNET_DVR_DVR_NET_DISK_DEL_ = struct_tagNET_DVR_DVR_NET_DISK_DEL_
