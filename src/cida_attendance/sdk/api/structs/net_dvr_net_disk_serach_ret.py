from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_NET_DISK_SERACH_RET(Structure):
    pass

_S(struct_tagNET_DVR_NET_DISK_SERACH_RET, [
    ('byDirectory', BYTE * 128),
    ('byRes', BYTE * 20),
])

NET_DVR_NET_DISK_SERACH_RET = struct_tagNET_DVR_NET_DISK_SERACH_RET
LPNET_DVR_NET_DISK_SERACH_RET = POINTER(struct_tagNET_DVR_NET_DISK_SERACH_RET)
tagNET_DVR_NET_DISK_SERACH_RET = struct_tagNET_DVR_NET_DISK_SERACH_RET
