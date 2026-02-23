from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_optical_dev_node import NET_DVR_OPTICAL_DEV_NODE


class struct_tagNET_DVR_OPTICAL_PORT_INFO(Structure):
    pass

_S(struct_tagNET_DVR_OPTICAL_PORT_INFO, [
    ('dwSize', DWORD),
    ('byValid', BYTE),
    ('byLinkType', BYTE),
    ('byPortWorkMode', BYTE),
    ('byRes1', BYTE * 1),
    ('dwPairPort', DWORD),
    ('struDevInfo', NET_DVR_OPTICAL_DEV_NODE * 32),
    ('byRes2', BYTE * 32),
])

NET_DVR_OPTICAL_PORT_INFO = struct_tagNET_DVR_OPTICAL_PORT_INFO
LPNET_DVR_OPTICAL_PORT_INFO = POINTER(struct_tagNET_DVR_OPTICAL_PORT_INFO)
tagNET_DVR_OPTICAL_PORT_INFO = struct_tagNET_DVR_OPTICAL_PORT_INFO
