from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_single_path import NET_VCA_SINGLE_PATH


class struct_tagNET_VCA_SAVE_PATH_CFG(Structure):
    pass

_S(struct_tagNET_VCA_SAVE_PATH_CFG, [
    ('dwSize', DWORD),
    ('struPathInfo', NET_VCA_SINGLE_PATH * 33),
    ('byRes', BYTE * 40),
])

NET_VCA_SAVE_PATH_CFG = struct_tagNET_VCA_SAVE_PATH_CFG
LPNET_VCA_SAVE_PATH_CFG = POINTER(struct_tagNET_VCA_SAVE_PATH_CFG)
tagNET_VCA_SAVE_PATH_CFG = struct_tagNET_VCA_SAVE_PATH_CFG
