from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_desc_node import NET_DVR_DESC_NODE


class struct_tagNET_DVR_DISKABILITY_LIST(Structure):
    pass

_S(struct_tagNET_DVR_DISKABILITY_LIST, [
    ('dwSize', DWORD),
    ('dwNodeNum', DWORD),
    ('struDescNode', NET_DVR_DESC_NODE * 256),
])

NET_DVR_DISKABILITY_LIST = struct_tagNET_DVR_DISKABILITY_LIST
LPNET_DVR_DISKABILITY_LIST = POINTER(struct_tagNET_DVR_DISKABILITY_LIST)
tagNET_DVR_DISKABILITY_LIST = struct_tagNET_DVR_DISKABILITY_LIST
