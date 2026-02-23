from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_rect import NET_VCA_RECT


class struct_tagNET_VCA_NORMAL_FIND(Structure):
    pass

_S(struct_tagNET_VCA_NORMAL_FIND, [
    ('dwImageID', DWORD),
    ('dwFaceScore', DWORD),
    ('struVcaRect', NET_VCA_RECT),
    ('byRes', BYTE * 20),
])

NET_VCA_NORMAL_FIND = struct_tagNET_VCA_NORMAL_FIND
LPNET_VCA_NORMAL_FIND = POINTER(struct_tagNET_VCA_NORMAL_FIND)
tagNET_VCA_NORMAL_FIND = struct_tagNET_VCA_NORMAL_FIND
