from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_mountmethod_param_union import NET_DVR_MOUNTMETHOD_PARAM_UNION


class struct_tagNET_DVR_SINGLE_NET_DISK_INFO_V40(Structure):
    pass

_S(struct_tagNET_DVR_SINGLE_NET_DISK_INFO_V40, [
    ('byNetDiskType', BYTE),
    ('byRes1', BYTE * 3),
    ('sDirectory', BYTE * 128),
    ('byDevAddr', BYTE * 64),
    ('wPort', WORD),
    ('byRes2', BYTE * 2),
    ('uMountMethodParam', NET_DVR_MOUNTMETHOD_PARAM_UNION),
    ('byRes4', BYTE * 80),
])

NET_DVR_SINGLE_NET_DISK_INFO_V40 = struct_tagNET_DVR_SINGLE_NET_DISK_INFO_V40
LPNET_DVR_SINGLE_NET_DISK_INFO_V40 = POINTER(struct_tagNET_DVR_SINGLE_NET_DISK_INFO_V40)
tagNET_DVR_SINGLE_NET_DISK_INFO_V40 = struct_tagNET_DVR_SINGLE_NET_DISK_INFO_V40
