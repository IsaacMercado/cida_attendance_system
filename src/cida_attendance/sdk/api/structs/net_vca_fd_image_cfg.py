from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_VCA_FD_IMAGE_CFG(Structure):
    pass

_S(struct_tagNET_VCA_FD_IMAGE_CFG, [
    ('dwWidth', DWORD),
    ('dwHeight', DWORD),
    ('dwImageLen', DWORD),
    ('byRes', BYTE * 20),
    ('pImage', POINTER(BYTE)),
])

NET_VCA_FD_IMAGE_CFG = struct_tagNET_VCA_FD_IMAGE_CFG
LPNET_VCA_FD_IMAGE_CFG = POINTER(struct_tagNET_VCA_FD_IMAGE_CFG)
tagNET_VCA_FD_IMAGE_CFG = struct_tagNET_VCA_FD_IMAGE_CFG
