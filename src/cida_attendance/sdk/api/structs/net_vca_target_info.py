from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_rect import NET_VCA_RECT


class struct_tagNET_VCA_TARGET_INFO(Structure):
    pass

_S(struct_tagNET_VCA_TARGET_INFO, [
    ('dwID', DWORD),
    ('struRect', NET_VCA_RECT),
    ('byRes', BYTE * 4),
])

NET_VCA_TARGET_INFO = struct_tagNET_VCA_TARGET_INFO
LPNET_VCA_TARGET_INFO = POINTER(struct_tagNET_VCA_TARGET_INFO)
tagNET_VCA_TARGET_INFO = struct_tagNET_VCA_TARGET_INFO
