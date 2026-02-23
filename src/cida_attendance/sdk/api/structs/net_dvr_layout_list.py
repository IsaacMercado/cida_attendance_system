from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_layoutcfg import NET_DVR_LAYOUTCFG


class struct_tagNET_DVR_LAYOUT_LIST(Structure):
    pass

_S(struct_tagNET_DVR_LAYOUT_LIST, [
    ('dwSize', DWORD),
    ('struLayoutInfo', NET_DVR_LAYOUTCFG * 16),
    ('byRes', BYTE * 4),
])

NET_DVR_LAYOUT_LIST = struct_tagNET_DVR_LAYOUT_LIST
LPNET_DVR_LAYOUT_LIST = POINTER(struct_tagNET_DVR_LAYOUT_LIST)
tagNET_DVR_LAYOUT_LIST = struct_tagNET_DVR_LAYOUT_LIST
