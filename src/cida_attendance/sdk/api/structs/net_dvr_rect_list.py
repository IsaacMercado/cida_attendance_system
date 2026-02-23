from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_vca_rect import NET_VCA_RECT


class struct_tagNET_DVR_RECT_LIST(Structure):
    pass

_S(struct_tagNET_DVR_RECT_LIST, [
    ('byRectNum', BYTE),
    ('byRes1', BYTE * 11),
    ('struVcaRect', NET_VCA_RECT * 6),
])

NET_DVR_RECT_LIST = struct_tagNET_DVR_RECT_LIST
LPNET_DVR_RECT_LIST = POINTER(struct_tagNET_DVR_RECT_LIST)
tagNET_DVR_RECT_LIST = struct_tagNET_DVR_RECT_LIST
