from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_rect import NET_VCA_RECT


class struct_tagNET_VCA_REGISTER_PIC(Structure):
    pass

_S(struct_tagNET_VCA_REGISTER_PIC, [
    ('dwImageID', DWORD),
    ('dwFaceScore', DWORD),
    ('struVcaRect', NET_VCA_RECT),
    ('byRes', BYTE * 20),
])

NET_VCA_REGISTER_PIC = struct_tagNET_VCA_REGISTER_PIC
LPNET_VCA_REGISTER_PIC = POINTER(struct_tagNET_VCA_REGISTER_PIC)
tagNET_VCA_REGISTER_PIC = struct_tagNET_VCA_REGISTER_PIC
