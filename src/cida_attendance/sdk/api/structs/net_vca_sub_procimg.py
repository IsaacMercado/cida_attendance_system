from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_rect import NET_VCA_RECT


class struct_tagNET_VCA_SUB_PROCIMG(Structure):
    pass

_S(struct_tagNET_VCA_SUB_PROCIMG, [
    ('dwImageLen', DWORD),
    ('dwFaceScore', DWORD),
    ('struVcaRect', NET_VCA_RECT),
    ('byRes', BYTE * 20),
    ('pImage', POINTER(BYTE)),
])

NET_VCA_SUB_PROCIMG = struct_tagNET_VCA_SUB_PROCIMG
LPNET_VCA_SUB_PROCIMG = POINTER(struct_tagNET_VCA_SUB_PROCIMG)
tagNET_VCA_SUB_PROCIMG = struct_tagNET_VCA_SUB_PROCIMG
