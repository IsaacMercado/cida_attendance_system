from ctypes import Structure, c_char

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_WPA_CFG(Structure):
    pass

_S(struct_tagNET_DVR_WPA_CFG, [
    ('byAlgorithmType', BYTE),
    ('byWPAKeyLen', BYTE),
    ('byDefaultPassword', BYTE),
    ('byRes1', BYTE),
    ('csSharedKey', c_char * 64),
    ('byRes', BYTE * 128),
])

NET_DVR_WPA_CFG = struct_tagNET_DVR_WPA_CFG
LPNET_DVR_WPA_CFG = POINTER(struct_tagNET_DVR_WPA_CFG)
tagNET_DVR_WPA_CFG = struct_tagNET_DVR_WPA_CFG
