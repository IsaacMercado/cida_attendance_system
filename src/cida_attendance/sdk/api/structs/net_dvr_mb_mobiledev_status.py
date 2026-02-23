from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .anon_351 import union_anon_351


class struct_tagNET_DVR_MB_MOBILEDEV_STATUS(Structure):
    pass

_S(struct_tagNET_DVR_MB_MOBILEDEV_STATUS, [
    ('dwSize', DWORD),
    ('mobileStatus', union_anon_351),
])

NET_DVR_MB_MOBILEDEV_STATUS = struct_tagNET_DVR_MB_MOBILEDEV_STATUS
LPNET_DVR_MB_MOBILEDEV_STATUS = POINTER(struct_tagNET_DVR_MB_MOBILEDEV_STATUS)
tagNET_DVR_MB_MOBILEDEV_STATUS = struct_tagNET_DVR_MB_MOBILEDEV_STATUS
