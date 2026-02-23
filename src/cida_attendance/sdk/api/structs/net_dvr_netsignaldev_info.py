from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_netsignal_info import NET_DVR_NETSIGNAL_INFO


class struct_tagNET_DVR_NETSIGNALDEV_INFO(Structure):
    pass

_S(struct_tagNET_DVR_NETSIGNALDEV_INFO, [
    ('struDevInfo', NET_DVR_NETSIGNAL_INFO),
    ('byRes1', BYTE * 816),
])

NET_DVR_NETSIGNALDEV_INFO = struct_tagNET_DVR_NETSIGNALDEV_INFO
LPNET_DVR_NETSIGNALDEV_INFO = POINTER(struct_tagNET_DVR_NETSIGNALDEV_INFO)
tagNET_DVR_NETSIGNALDEV_INFO = struct_tagNET_DVR_NETSIGNALDEV_INFO
