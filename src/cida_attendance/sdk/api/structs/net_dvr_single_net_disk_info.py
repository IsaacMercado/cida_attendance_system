from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR
from .net_dvr_mountmethod_param_union import NET_DVR_MOUNTMETHOD_PARAM_UNION


class struct_tagNET_DVR_SINGLE_NET_DISK_INFO(Structure):
    pass

_S(struct_tagNET_DVR_SINGLE_NET_DISK_INFO, [
    ('byNetDiskType', BYTE),
    ('byRes1', BYTE * 3),
    ('struNetDiskAddr', NET_DVR_IPADDR),
    ('sDirectory', BYTE * 128),
    ('wPort', WORD),
    ('byRes2', BYTE * 2),
    ('uMountMethodParam', NET_DVR_MOUNTMETHOD_PARAM_UNION),
    ('byRes3', BYTE * 8),
])

NET_DVR_SINGLE_NET_DISK_INFO = struct_tagNET_DVR_SINGLE_NET_DISK_INFO
LPNET_DVR_SINGLE_NET_DISK_INFO = POINTER(struct_tagNET_DVR_SINGLE_NET_DISK_INFO)
tagNET_DVR_SINGLE_NET_DISK_INFO = struct_tagNET_DVR_SINGLE_NET_DISK_INFO
